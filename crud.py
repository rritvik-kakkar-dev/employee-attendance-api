from sqlalchemy.orm import Session
from models import Employee, Attendance, User
from schemas import EmployeeCreate, AttendanceCreate, UserCreate
from datetime import datetime
from security import get_password_hash


#### EMPLOYEES ####
def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Employee).offset(skip).limit(limit).all()

def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()

def update_employee(db: Session, employee_id: int, employee: EmployeeCreate):
    db_employee = get_employee(db, employee_id)
    if db_employee:
        for key, value in employee.dict().items():
            setattr(db_employee, key, value)
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = get_employee(db, employee_id)
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee

#### ATTENDANCES ####
def create_attendance(db: Session, attendance: AttendanceCreate):
    db_attendance = Attendance(**attendance.dict())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

def get_attendances(db: Session, employee_id: int | None = None):
    query = db.query(Attendance)
    if employee_id:
        query = query.filter(Attendance.employee_id == employee_id)
    return query.all()

def checkout_attendance(db: Session, attendance_id: int):
    db_attendance = db.query(Attendance).filter(Attendance.id == attendance_id).first()
    if db_attendance and not db_attendance.check_out:
        db_attendance.check_out = datetime.now()
        hours = (db_attendance.check_out - db_attendance.check_in).total_seconds() / 3600
        db.commit()
        db.refresh(db_attendance)
        return db_attendance, hours
    return None, None

#### USERS ####
def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate) -> User:
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user