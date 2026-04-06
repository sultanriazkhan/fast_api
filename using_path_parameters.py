from fastapi import FastAPI
app = FastAPI(
    title="Meri pehli app",
    description="Yeh meri pehli API hai",
    version="1.0"
    
)
@app.get("/")
def age():
    return {"app": "FastAPI Practice", "version": "1.0"}
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "Fetched user": {user_id}}
@app.get("/users/{user_id}/items/{item_id}")
def get_user_item(user_id: int, item_id: int):
    return {
    "user_id":user_id,
    "item_id": item_id,
    "Fetched item": f"Item {item_id} for user {user_id}"
    }
    
@app.get("/products/{product_name}")
def get_product(product_name: str):
    return {"product": product_name, "in_stock": True}