from decimal import Decimal
from sqlalchemy import desc, select, func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.inventory_models import Inventory

def add_product(db:Session,data):
    inventory = Inventory(**data.model_dump())
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory
    
    
def get_all(db:Session):
    query = select(Inventory).order_by(Inventory.product_id)
    result = db.scalars(query).all()
    return result    

def get_by_id(db:Session, product_id:int):
    return db.get(Inventory, product_id)

def update(db:Session, product_id:int, data):
    inventory = db.get(Inventory,product_id)
    if inventory is None:
        return None
    for Key,Value in data.model_dump().items():
        setattr(inventory,Key,Value)
        
    try:
        db.commit()
        db.refresh(inventory)
        return inventory
    except IntegrityError:
        db.rollback()
        raise    
    
    
def delete(db:Session, product_id:int):
    inventory = db.get(Inventory, product_id)
    if inventory is None:
        return None
    db.delete(inventory)
    db.commit()
    return True    

def by_category(db:Session, category:str):
    query = select(Inventory).where(
        Inventory.category == category
    )
    result = db.scalars(query).all()
    return result

def low_stock(db:Session):
    query = select(Inventory).where(
       Inventory.quantity_in_stock < Inventory.recorder_level 
    )
    result = db.scalars(query).all()
    return result


def increase_stock(db: Session, product_id: int, quantity: int):
    inventory = db.get(Inventory, product_id)

    if inventory is None:
        return None

    if quantity <= 0:
        return False

    inventory.stock_quantity += quantity

    db.commit()
    db.refresh(inventory)

    return inventory


def decrease_stock(db: Session, product_id: int, quantity: int):
    inventory = db.get(Inventory, product_id)

    if inventory is None:
        return None

    if quantity <= 0:
        return False

    if inventory.stock_quantity < quantity:
        return False

    inventory.stock_quantity -= quantity

    db.commit()
    db.refresh(inventory)

    return inventory


def total_revenue(db:Session):
    query = select(func.sum(Inventory.unit_price * Inventory.quantity_in_stock))
    return db.scalars(query)