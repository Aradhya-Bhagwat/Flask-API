from fastapi import Depends, FastAPI, HTTPException, status
from models import Products
from database import SessionLocal, engine
import database_models
from sqlalchemy.orm import Session
app = FastAPI()

database_models.Base.metadata.create_all(bind = engine)

@app.get('/')
def greet():
    return ("Welcome to my first Flask API using uvicorn server")

products = [
    Products(id=1, name="Asus Vivobook S14", description="Windows Laptop", price=60000, qty=10),
    Products(id=2, name="MacBook Air M4", description="Apple Laptop", price=90000, qty=5),
    Products(id=3, name="Dell Inspiron 15", description="Windows Laptop", price=55000, qty=8),
    Products(id=4, name="HP Pavilion 14", description="Windows Laptop", price=62000, qty=7),
    Products(id=5, name="Lenovo IdeaPad Slim 5", description="Windows Laptop", price=58000, qty=12),
    Products(id=6, name="Samsung Galaxy S25", description="Android Smartphone", price=75000, qty=15),
    Products(id=7, name="iPhone 16", description="Apple Smartphone", price=80000, qty=10),
    Products(id=8, name="Sony WH-1000XM5", description="Wireless Headphones", price=30000, qty=20),
    Products(id=9, name="Apple iPad Air", description="Tablet", price=65000, qty=6),
    Products(id=10, name="Logitech MX Master 3S", description="Wireless Mouse", price=9000, qty=25)
]

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()

def db_init():
    db = SessionLocal()
    try:
        for product in products:
            existing_product = db.get(database_models.Products, product.id)
            if existing_product is None:
                db.add(database_models.Products(**product.model_dump()))
        db.commit()
    finally:
        db.close()


db_init()

@app.get('/products')
@app.get('/products/')
def get_all_products(db : Session = Depends(get_db) ):
    db_products = db.query(database_models.Products).all()
    return [Products.model_validate(product) for product in db_products]

@app.get('/products/{id}')
@app.get('/product/{id}')
def get_product_by_id(id : int, db : Session = Depends(get_db)):
    product = db.get(database_models.Products, id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return Products.model_validate(product)

@app.post('/products', status_code=status.HTTP_201_CREATED)
@app.post('/products/')
@app.post('/product')
def add_product(product : Products, db : Session = Depends(get_db)):
    if db.get(database_models.Products, product.id) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Product already exists")
    db_product = database_models.Products(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return Products.model_validate(db_product)

@app.put('/products/{id}')
@app.put('/product/{id}')
def update_product(id : int, product : Products, db : Session = Depends(get_db)):
    db_product = db.get(database_models.Products, id)
    if db_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    for field, value in product.model_dump().items():
        setattr(db_product, field, value)
    db.commit()
    db.refresh(db_product)
    return Products.model_validate(db_product)

@app.delete('/products/{id}')
@app.delete('/product/{id}')
def delete_product(id : int, db : Session = Depends(get_db)):
    db_product = db.get(database_models.Products, id)
    if db_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}