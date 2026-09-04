from fastapi import FastAPI
from models import Products
app = FastAPI()

@app.get('/')
def greet():
    return ("Welcome to my first Flask API using uvicorn server")

products = [
    Products(id = 1, name = "Asus Vivobook S14", description = "Windows Laptop", price = "60000", qty = "10"),
    Products(id = 2, name = "Macbook", description = "Air M4", price = "90000", qty = "5")
]

@app.get('/products')
def get_all_products():
    return products

@app.get('/product/{id}')
def get_product_by_id(id : int):
    for product in products:
        if id == product.id:
            return product
    return "Product Not Found !"

@app.post('/product')
def add_product(product : Products):
    products.append(product)

@app.put('/product')
def update_product(id : int, product : Products):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Added Successfully !"
    return "Product Not Found !"

@app.delete('/product')
def delete_product(id : int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted Successfully !"
    return "Product Not Found !"