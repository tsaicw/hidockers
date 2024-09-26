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

channel.queue_declare(queue='hello')

message = 'Hello, World!'
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body=message,
)

print(f' [x] Sent {message}')
connection.close()
