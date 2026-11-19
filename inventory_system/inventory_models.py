from sqlalchemy import Numeric, String, Boolean, DECIMAL,Integer, Column
from config.database import Base

class Inventory(Base):
    __tablename__ = "inventory"
    
    product_id = Column(
        Integer,
        primary_key=True,
        index=True,
        nullable=False
    )
    product_name = Column(
        String(100),
        nullable=False
    )
    category = Column(
        String(30),
        nullable=False
    )
    supplier_name = Column(
        String(40),
        nullable=False
    )
    unit_price = Column(
        DECIMAL(ge = 0),
        nullable=False,
        )
    quantity_in_stock = Column(
        Integer,
        nullable=False
    )
    recorder_level = Column(
        Integer,
        nullable=False
    )
    warehouse_location = Column(
        String(200),
        nullable=False
    )
    is_active= Column(
        Boolean,
        nullable=False
    )
    