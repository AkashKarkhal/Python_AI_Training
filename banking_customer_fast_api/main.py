from fastapi import FastAPI
from config.database import SessionLocal,Base,engine
from schemas.banking_schemas import CustomerCreate, CustomerResponse
from services import banking_services as services
from schemas.banking_schemas import *


app = FastAPI(
    title="jadbfdaf",
    version="41;0;14"
)
Base.metadata.create_all(bind=engine)


@app.post("/open_account", response_model=CustomerResponse)
def open_account(data: CustomerCreate):
    db = SessionLocal()
    return services.open_account(db, data)


@app.get("/accounts", response_model=list[CustomerResponse])
def get_all_accounts(page: int = 1, size: int = 10):
    db = SessionLocal()
    return services.get_all_accounts(db, page, size)


@app.get("/account/{account_number}",
         response_model=CustomerResponse)
def get_account(account_number: str):
    db = SessionLocal()
    return services.get_account_by_number(db, account_number)


@app.put("/update/{account_number}",
         response_model=CustomerResponse)
def update_customer(
    account_number: str,
    data: CustomerUpdate
):
    db = SessionLocal()
    return services.update_customer(
        db,
        account_number,
        data
    )


@app.delete("/close/{account_number}")
def close_account(account_number: str):
    db = SessionLocal()
    return services.close_account(
        db,
        account_number
    )


@app.get("/branch/{branch_name}",
         response_model=list[CustomerResponse])
def filter_branch(branch_name: str):
    db = SessionLocal()
    return services.filter_by_branch(
        db,
        branch_name
    )


@app.get("/account_type/{account_type}",
         response_model=list[CustomerResponse])
def filter_account_type(account_type: str):
    db = SessionLocal()
    return services.filter_by_account_type(
        db,
        account_type
    )


@app.put("/deposit/{account_number}",
         response_model=CustomerResponse)
def deposit(
    account_number: str,
    amount: float
):
    db = SessionLocal()
    return services.deposit_amount(
        db,
        account_number,
        amount
    )


@app.put("/withdraw/{account_number}",
         response_model=CustomerResponse)
def withdraw(
    account_number: str,
    amount: float
):
    db = SessionLocal()
    return services.withdraw_amount(
        db,
        account_number,
        amount
    )


@app.get("/total_deposit_branch")
def total_deposit_branch():
    db = SessionLocal()
    return services.total_deposit_by_branch(db)