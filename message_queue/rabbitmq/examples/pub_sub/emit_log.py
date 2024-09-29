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

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or 'Hello, World!'
channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message
)

print(f' [x] Sent {message}')
connection.close()
