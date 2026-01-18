from fastapi import APIRouter
from sqlalchemy.orm import Session
from database import get_db
import crud
import schemas
from config import get_settings, Settings
from fastapi.middleware.cors import CORSMiddleware
from routers import auth
from security import get_current_user
from models import User
from fastapi import Depends, HTTPException

router = APIRouter(
    prefix="/attendances",
    tags=["Attendances"],          # ← This creates the group
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Attendance)
def create_attendance(attendance: schemas.AttendanceCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.create_attendance(db, attendance)

@router.get("/", response_model=list[schemas.Attendance])
def read_attendances(employee_id: int | None = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.get_attendances(db, employee_id)

@router.put("/{attendance_id}/checkout")
def checkout_attendance(attendance_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    attendance, hours = crud.checkout_attendance(db, attendance_id)
    if attendance is None:
        raise HTTPException(status_code=404, detail="Attendance not found or already checked out")
    return {"message": "Checked out", "hours_worked": hours}
