import asyncio
from .connection import RabbitMQConnection
import aio_pika

import json

async def publish_event(exchange_name: str, routing_key: str, payload: dict):
    channel = await RabbitMQConnection.get_channel()
    exchange = await channel.declare_exchange(exchange_name, aio_pika.ExchangeType.TOPIC)
    message_body = json.dumps(payload).encode()
    message = aio_pika.Message(message_body)
    await exchange.publish(message, routing_key=routing_key)
    print(f"[Publisher] Event sent to {exchange_name}:{routing_key}")