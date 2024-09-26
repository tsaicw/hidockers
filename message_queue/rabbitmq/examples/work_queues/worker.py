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

    channel.queue_declare(queue='task_queue', durable=True)

    def callback(ch, method, properties, body):
        print(f' [x] Received {body.decode()}')
        time.sleep(body.count(b'.'))
        print(' [x] Done')
        ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue='task_queue',
        auto_ack=False,
        on_message_callback=callback
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
