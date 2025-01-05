import asyncio
from rstream import Producer

USERNAME = 'guest'
PASSWORD = 'guest'
RABBITMQ_HOST = 'localhost'

STREAM_NAME = 'hello-python-stream'
STREAM_RETENTION = 5000000000  # 5GB

async def send():
    async with Producer(
        host=RABBITMQ_HOST,
        port=5552,
        username=USERNAME,
        password=PASSWORD
    ) as producer:
        await producer.create_stream(STREAM_NAME, exists_ok=True, arguments={'MaxLengthBytes': STREAM_RETENTION})
        await producer.send(stream=STREAM_NAME, message=b'Hello, World!')

        print(' [x] Hello, World! message sent')
        input(' [x] Press Enter to close the Producer ...')

asyncio.run(send())
