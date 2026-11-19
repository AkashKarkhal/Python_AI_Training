from sqlalchemy import Column, Integer, String, Boolean, Date, DECIMAL
from config.database import Base

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    account_number = Column(String(50), unique=True, nullable=False)
    account_type = Column(String(20), nullable=False)
    branch_name = Column(String(100), nullable=False)
    balance = Column(DECIMAL(12, 2), nullable=False, default=0)
    is_active = Column(Boolean, default=True)
    opened_on = Column(Date, nullable=False)