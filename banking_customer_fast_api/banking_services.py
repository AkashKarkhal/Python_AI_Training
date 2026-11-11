from sqlalchemy import select, func
from models.banking_models import Customer


def open_account(db, data):
    customer = Customer(**data.model_dump())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


def get_all_accounts(db, page: int, size: int):
    query = (
        select(Customer)
        .offset((page - 1) * size)
        .limit(size)
    )
    return db.scalars(query).all()


def get_account_by_number(db, account_number: str):
    query = select(Customer).where(
        Customer.account_number == account_number
    )
    return db.scalar(query)


def update_customer(db, account_number: str, data):
    customer = db.scalar(
        select(Customer).where(
            Customer.account_number == account_number
        )
    )

    if not customer:
        return None

    customer.email = data.email
    customer.branch_name = data.branch_name

    db.commit()
    db.refresh(customer)
    return customer


def close_account(db, account_number: str):
    customer = db.scalar(
        select(Customer).where(
            Customer.account_number == account_number
        )
    )

    if not customer:
        return False

    if customer.balance != 0:
        return "Balance must be zero"

    db.delete(customer)
    db.commit()
    return True


def filter_by_branch(db, branch_name: str):
    query = select(Customer).where(
        Customer.branch_name == branch_name
    )
    return db.scalars(query).all()


def filter_by_account_type(db, account_type: str):
    query = select(Customer).where(
        Customer.account_type == account_type
    )
    return db.scalars(query).all()


def deposit_amount(db, account_number: str, amount: float):
    customer = db.scalar(
        select(Customer).where(
            Customer.account_number == account_number
        )
    )

    if not customer or not customer.is_active:
        return None

    customer.balance += amount

    db.commit()
    db.refresh(customer)
    return customer


def withdraw_amount(db, account_number: str, amount: float):
    customer = db.scalar(
        select(Customer).where(
            Customer.account_number == account_number
        )
    )

    if not customer or not customer.is_active:
        return None

    if customer.balance < amount:
        return "Insufficient Balance"

    customer.balance -= amount

    db.commit()
    db.refresh(customer)
    return customer


def total_deposit_by_branch(db):
    query = (
        select(
            Customer.branch_name,
            func.sum(Customer.balance).label("total_balance")
        )
        .group_by(Customer.branch_name)
    )

    result = db.execute(query).all()

    return [
        {
            "branch_name": row.branch_name,
            "total_balance": row.total_balance
        }
        for row in result
    ]