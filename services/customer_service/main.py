from fastapi import FastAPI
from pydantic import BaseModel
# from patterns.messaging.messaging import publish_event
from patterns.messaging.publisher import publish_event


app = FastAPI()

# In-memory storage (for demo)
CUSTOMERS = {}

class CustomerCreate(BaseModel):
    name: str
    email: str

@app.post("/customers")
async def create_customer(customer: CustomerCreate):
    # Simulate storing in DB
    customer_id = len(CUSTOMERS) + 1
    CUSTOMERS[customer_id] = customer.dict()

    # Publish event to RabbitMQ
    event = {
        "event_type": "CustomerCreated",
        "data": {
            "customer_id": customer_id,
            "name": customer.name,
            "email": customer.email
        }
    }
    await publish_event("customer_events", "customer.created", event)

    return {"id": customer_id, **customer.dict()}

# give you a small Python snippet that will ensure the queue exists, is durable, and is properly bound to your exchange automatically. This is exactly what you need for your setup.