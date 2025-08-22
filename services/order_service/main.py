import asyncio
import aio_pika
from patterns.messaging.connection import RabbitMQConnection

RABBITMQ_URL = "amqp://guest:guest@rabbitmq:5672/"


async def handle_order_event(message: aio_pika.IncomingMessage):
    async with message.process():  # automatically ack
        print("Received event in Order Service:", message.body.decode())


async def main():
    channel = await RabbitMQConnection.get_channel()

    # Declare exchange
    exchange = await channel.declare_exchange(
        "customer_events", aio_pika.ExchangeType.TOPIC
    )

    # Declare queue
    queue = await channel.declare_queue("order_queue", durable=True)

    # Bind queue to exchange with routing key
    await queue.bind(exchange, routing_key="customer.created")

    # Start consuming
    await queue.consume(handle_order_event)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    # Keep the program running
    await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
