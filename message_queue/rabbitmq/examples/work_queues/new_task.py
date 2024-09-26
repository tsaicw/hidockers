import pika, sys

USERNAME='guest'
PASSWORD='guest'
RABBITMQ_HOST='localhost'

credentials = pika.PlainCredentials(username=USERNAME, password=PASSWORD)
parameters = pika.ConnectionParameters(host=RABBITMQ_HOST,
                                       port=5672,
                                       virtual_host='/',
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or 'Hello, World!'
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent
    )
)

print(f' [x] Sent {message}')
connection.close()
