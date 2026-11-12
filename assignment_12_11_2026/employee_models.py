from sqlalchemy import Numeric, String, DECIMAL, Boolean
from config.database import Base

class PayrollBase(Base):
    __tablename__="payrolldata"
    
    