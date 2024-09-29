import pika, sys, os, time

USERNAME='guest'
PASSWORD='guest'
RABBITMQ_HOST='localhost'

def main():
    credentials = pika.PlainCredentials(username=USERNAME, password=PASSWORD)
    parameters = pika.ConnectionParameters(host=RABBITMQ_HOST,
                                           port=5672,
                                           virtual_host='/',
                                           credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    binding_keys = sys.argv[1:]
    if not binding_keys:
        sys.stderr.write(f'Usage: {sys.argv[0]} [binding_key]...\n')
        sys.exit(1)

    for binding_key in binding_keys:
        channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)

    channel.basic_consume(
        queue=queue_name,
        auto_ack=True,
        on_message_callback=lambda ch, method, properties, body: print(f' [x] {method.routing_key}:{body.decode()}')
    )

    print(' [*] Waiting for logs. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interruptd')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
