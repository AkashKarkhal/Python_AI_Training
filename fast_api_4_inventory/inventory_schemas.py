from decimal import Decimal
from xmlrpc.client import Boolean
from pydantic import (BaseModel, Field,EmailStr,ConfigDict)

class InventoryBase(BaseModel):
    product_name: str = Field(min_length=2)
    Category: str = Field(min_length=2)
    supplier_name: str = Field(min_length=2)
    Unit_price: int = Field(ge=0)
    quantity_in_stock: int = Field(ge = 0)
    recorder_level: int = Field(ge=0)
    warehouse_location: str = Field(min_length=2)
    is_active: bool = True    
    
class InventoryCreate(InventoryBase):
    pass    
class InventoryUpdate(InventoryBase):
    pass
class InventoryReponse(InventoryBase):
    product_id:int
    model_config = ConfigDict(from_attributes=True)
