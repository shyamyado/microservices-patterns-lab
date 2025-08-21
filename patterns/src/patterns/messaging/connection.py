import os
import aio_pika

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672")

class RabbitMQConnection:
    _connection = None
    _channel = None

    @classmethod
    async def get_channel(cls):
        if cls._channel is None or cls._channel.is_closed:
            if cls._connection is None or cls._connection.is_closed:
                cls._connection = await aio_pika.connect_robust(RABBITMQ_URL)
            cls._channel = await cls._connection.channel()
        return cls._channel

    @classmethod
    async def close(cls):
        if cls._channel and not cls._channel.is_closed:
            await cls._channel.close()
        if cls._connection and not cls._connection.is_closed:
            await cls._connection.close()
        cls._channel = None
        cls._connection = None
