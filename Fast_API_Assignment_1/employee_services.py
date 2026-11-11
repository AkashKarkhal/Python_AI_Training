from decimal import Decimal
from sqlalchemy import desc, select, func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.employee_moedels import Employee

def add_employee(db:Session, data):
    employee = Employee(**data.model_dump())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def get_emp_by_id(db:Session, employee_id:int):
    return db.get(Employee, employee_id)

def update_employee(db:Session, employee_id:int, data):
    employee = db.get(Employee, employee_id)
    if employee is None:
        return None
    for Key, value in data.model_dump().items():
        setattr(employee,Key, value)
        
        
    try:
        db.commit()
        db.refresh(employee)
        return employee  
    
    except IntegrityError:
        db.rollback()
        raise  
    
def delete_emp(db:Session, employee_id):
    employee = db.get(Employee, employee_id)
    if employee is None:
        return False
    
    db.delete(employee)
    db.commit()
    return True

def get_by_dept(db:Session, department:str):
    query = select(Employee).where(
        Employee.department == department
    )

    return db.scalars(query).all()
    
def get_top_performer(db:Session, performance_rating:float):
    query = select(Employee).where(
        Employee.performance_rating == performance_rating
    )
    return db.scalars(query).all()
    

def avg_rating_by_dept(db:Session):
    query = (
       select(
           Employee.department, func.avg(Employee.performance_rating).label("average_rating")
           
       ) .group_by(Employee.department)
    )
    return db.execute(query).all()
      
      
def top_five_employees(db:Session):
    query = (
        select(Employee).order_by(desc(Employee.performance_rating)).limit(5)
    )     
    return db.scalars(query).all() 


def classify_employees(db):

    employees = db.query(Employee).all()

    result = []

    for emp in employees:

        if emp.performance_rating >= 4.5:
            category = "Outstanding"

        elif emp.performance_rating >= 3.5:
            category = "Good"

        else:
            category = "Needs Improvement"

        result.append({
            "employee_id": emp.employee_id,
            "employee_name": emp.employee_name,
            "category": category
        })

    return result
    