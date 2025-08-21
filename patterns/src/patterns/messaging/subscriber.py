import asyncio
from .connection import RabbitMQConnection
import aio_pika


async def subscribe(exchange_name: str, routing_key: str, queue_name: str, callback):
    channel = await RabbitMQConnection.get_channel()
    exchange = await channel.declare_exchange(exchange_name, aio_pika.ExchangeType.TOPIC)
    queue = await channel.declare_queue(queue_name, durable=True)
    await queue.bind(exchange, routing_key)

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                await callback(message.body)