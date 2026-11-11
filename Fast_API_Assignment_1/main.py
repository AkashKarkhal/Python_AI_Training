from fastapi import FastAPI
from config.database import Base, SessionLocal, engine
from schemas.employee_schemas import DepartmentAverage, EmployeeResponse, EmployeeCreate, EmployeeUpdate
from services import employee_services as service

app = FastAPI(
    title="Fast API",
    version="41:0:14"
)

Base.metadata.create_all(bind=engine)

@app.post("/add", response_model=EmployeeResponse)
def add_employee(data:EmployeeCreate):
    db = SessionLocal()
    return service.add_employee(db, data)

@app.get("/getempppbyid/{employee_id}", response_model=EmployeeResponse)
def get_emp_by_id(employee_id:int):
    db = SessionLocal()
    return service.get_emp_by_id(db, employee_id) 

@app.put("/update/{employee_id}", response_model=EmployeeResponse)
def get_update(employee_id:int, data:EmployeeUpdate):
    db = SessionLocal()
    return service.update_employee(db,employee_id, data)
    
@app.delete("/delete/{employee_id}")
def delete(employee_id: int):
    db = SessionLocal()

    deleted = service.delete_emp(db, employee_id)

    if deleted:
        return {"message": "Employee deleted successfully"}

    return {"message": "Employee not found"}   

@app.get("/get_dept/{department}", response_model=list[EmployeeResponse])
def get_emp_by_dept(department:str):
    db = SessionLocal()
    return service.get_by_dept(db,department)

@app.get("/top_performer", response_model=list[EmployeeResponse])
def top_performer(performance_rating:float):
    db =SessionLocal()
    return service.get_top_performer(db, performance_rating)

@app.get("/avg_rating",response_model=list[DepartmentAverage])
def avg_rating():
    db = SessionLocal()
    return service.avg_rating_by_dept(db)

@app.get("/highest_rated")
def highest_rated():
    db = SessionLocal()
    return service.top_five_employees(db)

@app.get("/classify")
def classify():
    db=SessionLocal()
    return service.classify_employees(db)