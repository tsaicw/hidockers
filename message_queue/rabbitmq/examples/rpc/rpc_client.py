import pika, sys, uuid

USERNAME='guest'
PASSWORD='guest'
RABBITMQ_HOST='localhost'

class FibonacciRpcClient(object):
    def __init__(self):
        credentials = pika.PlainCredentials(username=USERNAME, password=PASSWORD)
        parameters = pika.ConnectionParameters(
                            host=RABBITMQ_HOST,
                            port=5672,
                            virtual_host='/',
                            credentials=credentials
                        )
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            auto_ack=True,
            on_message_callback=self.on_response
        )

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, properties, body):
        if self.corr_id == properties.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())

        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            body=str(n),
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id
            )
        )

        while self.response is None:
            self.connection.process_data_events(time_limit=None)

        return int(self.response)

fibonacci_rpc = FibonacciRpcClient()

for n in sys.argv[1:]:
    print(f' [x] Requesting fib({n})')
    response = fibonacci_rpc.call(n)
    print(f' [.] Got {response}')

fibonacci_rpc.connection.close()
