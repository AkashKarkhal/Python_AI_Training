from fastapi import FastAPI
from config.database import Base, SessionLocal, engine
from schemas.inventory_schemas import InventoryBase, InventoryCreate, InventoryReponse,InventoryUpdate
from services import inventory_services as sv

app = FastAPI(
    title="fast api",
    version="41:04:14"
)
Base.metadata.create_all(bind=engine)

@app.post("/add",response_model=InventoryReponse)
def add_product(data:InventoryCreate):
    db = SessionLocal()
    return sv.add_product(db,data)

@app.get("all",response_model=list[InventoryReponse])
def get_all():
    db = SessionLocal()
    return sv.get_all(db)
@app.get("/id/{product_id}",response_model=InventoryReponse)
def by_id(product_id:int):
    db = SessionLocal()
    return sv.get_by_id(db)

@app.put("/update/{product_id}", response_model=InventoryReponse)
def update(product_id:int, data:InventoryUpdate):
    db = SessionLocal()
    return sv.update(db,product_id,data)


@app.delete("/delete/{product_id}", response_model=InventoryReponse)
def delete(product_id:int):
    db = SessionLocal()
    deleted = sv.delete(db,product_id)
    if deleted:
        return {"message": "Employee deleted done"}
    return {"message":"Employee not found"}

@app.get("by_category", response_model=InventoryReponse)
def category(category:str):
    db = SessionLocal()
    return sv.by_category(db,category)

@app.get("low_stock", response_model=InventoryReponse)
def low_stock():
    db = SessionLocal()
    return sv.low_stock(db)

@app.put("/increase-stock/{product_id}",
         response_model=InventoryReponse)
def increase_stock(product_id: int, quantity_in_stock: int):
    db = SessionLocal()
    return sv.increase_stock(db, product_id, quantity_in_stock)



@app.put("/decrease-stock/{product_id}",
         response_model=InventoryReponse)
def decrease_stock(product_id: int, quantity_in_stock: int):
    db = SessionLocal()
    return sv.decrease_stock(db, product_id, quantity_in_stock)


@app.get("/inventory", response_model=InventoryReponse)
def value():
    db = SessionLocal()
    return {
        "total_inventory_value":
            sv.total_revenue(db)
    }