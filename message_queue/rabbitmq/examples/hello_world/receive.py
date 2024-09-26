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

    channel.queue_declare(queue='hello')

    channel.basic_consume(
        queue='hello',
        auto_ack=True,
        on_message_callback=lambda ch, method, propertiews, body: print(f' [x] Received {body.decode()}')
    )

    print(' [*] Waiting for messages. To exit press CTRL+C')
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
