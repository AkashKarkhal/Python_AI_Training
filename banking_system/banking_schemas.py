from pydantic import BaseModel, Field, EmailStr
from datetime import date
from decimal import Decimal
from typing import Literal

class CustomerBase(BaseModel):
    customer_name: str
    email: EmailStr
    account_number: str
    account_type: Literal["Savings", "Current"]
    branch_name: str
    balance: Decimal = Field(ge=0)
    is_active: bool
    opened_on: date


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    customer_name: str | None = None
    email: EmailStr | None = None
    account_number: str | None = None
    account_type: Literal["Savings", "Current"] | None = None
    branch_name: str | None = None
    balance: Decimal | None = Field(default=None, ge=0)
    is_active: bool | None = None
    opened_on: date | None = None


class CustomerResponse(CustomerBase):
    customer_id: int

    model_config = {
        "from_attributes": True
    }
