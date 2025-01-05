import asyncio
import signal

from rstream import (
    AMQPMessage,
    Consumer,
    MessageContext,
    ConsumerOffsetSpecification,
    OffsetType
)

USERNAME = 'guest'
PASSWORD = 'guest'
RABBITMQ_HOST = 'localhost'

STREAM_NAME = 'hello-python-stream'
STREAM_RETENTION = 5000000000  # 5GB

async def receive():
    async with Consumer(
        host=RABBITMQ_HOST,
        port=5552,
        username=USERNAME,
        password=PASSWORD
    ) as consumer:
        await consumer.create_stream(STREAM_NAME, exists_ok=True, arguments={"MaxLengthBytes": STREAM_RETENTION})

        async def on_message(msg: AMQPMessage, message_context: MessageContext):
            stream = message_context.consumer.get_stream(message_context.subscriber_name)
            print(f'Got message: {msg} from stream {stream}')

        print('Press CTRL+C to close')
        await consumer.start()
        await consumer.subscribe(
            stream=STREAM_NAME,
            callback=on_message,
            offset_specification=ConsumerOffsetSpecification(OffsetType.FIRST, None)
        )

        try:
            await consumer.run()
        except (KeyboardInterrupt, asyncio.CancelledError):
            print('Closing Consumer ...')
            return

asyncio.run(receive())
