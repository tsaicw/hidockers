import pika, sys, os, time

USERNAME='guest'
PASSWORD='guest'
RABBITMQ_HOST='localhost'

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    credentials = pika.PlainCredentials(username=USERNAME, password=PASSWORD)
    parameters = pika.ConnectionParameters(host=RABBITMQ_HOST,
                                           port=5672,
                                           virtual_host='/',
                                           credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='rpc_queue')

    def on_request(ch, method, properties, body):
        n = int(body)

        print(f' [.] fib({n})')
        response = fib(n)

        ch.basic_publish(
            exchange='',
            routing_key=properties.reply_to,
            body=str(response),
            properties=pika.BasicProperties(
                correlation_id=properties.correlation_id
            )
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue='rpc_queue',
        auto_ack=False,
        on_message_callback=on_request
    )

    print(' [*] Awaiting RPC requests. To exit press CTRL+C')
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
