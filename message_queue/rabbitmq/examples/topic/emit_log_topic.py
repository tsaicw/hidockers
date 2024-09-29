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

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello, World!'
channel.basic_publish(
    exchange='topic_logs',
    routing_key=routing_key,
    body=message
)

print(f' [x] Sent {routing_key}:{message}')
connection.close()
