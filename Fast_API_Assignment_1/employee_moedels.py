from sqlalchemy import Column, Integer, String, Numeric, Float
from config.database import Base


class Employee(Base):
    __tablename__ = "Employee"

    employee_id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    employee_name = Column(
        String(30),
        nullable=False
    )

    department = Column(
        String(20),
        nullable=False
    )

    designation = Column(
        String(30),
        nullable=False
    )

    salary = Column(
        Numeric(12, 2),
        nullable=False
    )

    performance_rating = Column(
        Float,
        nullable=False
    )

    projects_completed = Column(
        Integer,
        nullable=False
    )

    attendance_percentage = Column(
        Float,
        nullable=False
    )

    review_year = Column(
        Integer,
        nullable=False
    )