import asyncio
import aio_pika

async def test():
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost:5672/")
    print("Connected to RabbitMQ!")
    await connection.close()

asyncio.run(test())
