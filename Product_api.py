from fastapi import FastAPI
app = FastAPI()
@app.get("/products/{product_id}")
def read_product(
    product_id: int ,
    category: str= "Food",
    in_stock: bool = True,
    name: str = "Kajo Katli",
    price: float=9.99
    ):
    return {
        "product_id":product_id,
        "category":category,
        "in_stock": in_stock,
        "name": name,
        "price": price
        
    }
  