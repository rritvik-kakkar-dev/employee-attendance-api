from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud
import schemas
from config import get_settings, Settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Employee & Attendance API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",     # Vite default dev port
        "http://localhost:3000",     # if using create-react-app
        "http://127.0.0.1:5173",
        # Add your production frontend domain later, e.g. "https://your-app.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Employee routes
@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)

@app.get("/employees/", response_model=list[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_employees(db, skip, limit)

@app.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.put("/employees/{employee_id}", response_model=schemas.Employee)
def update_employee(employee_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    updated = crud.update_employee(db, employee_id, employee)
    if updated is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_employee(db, employee_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted"}


# Attendance routes
@app.post("/attendances/", response_model=schemas.Attendance)
def create_attendance(attendance: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    return crud.create_attendance(db, attendance)

@app.get("/attendances/", response_model=list[schemas.Attendance])
def read_attendances(employee_id: int | None = None, db: Session = Depends(get_db)):
    return crud.get_attendances(db, employee_id)

@app.put("/attendances/{attendance_id}/checkout")
def checkout_attendance(attendance_id: int, db: Session = Depends(get_db)):
    attendance, hours = crud.checkout_attendance(db, attendance_id)
    if attendance is None:
        raise HTTPException(status_code=404, detail="Attendance not found or already checked out")
    return {"message": "Checked out", "hours_worked": hours}


# Report routes
@app.get("/reports/{employee_id}")
def get_report(employee_id: int, db: Session = Depends(get_db)):
    attendances = crud.get_attendances(db, employee_id)
    total_hours = sum((a.check_out - a.check_in).total_seconds() / 3600 for a in attendances if a.check_out)
    return {"employee_id": employee_id, "total_hours": total_hours}