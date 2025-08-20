from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

DATABASE_URL = "postgresql://customer_user:customer_pass@customer_db:5432/demo"
engine = create_engine(DATABASE_URL)

@app.get("/")
def root():
    return {"message": "Customer service is up!"}

@app.get("/customers")
def get_customers():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1 as id, 'John Doe' as name"))
        return [dict(row) for row in result]


        
