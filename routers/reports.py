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
    prefix="/reports",
    tags=["Reports"],          # ← This creates the group
    responses={404: {"description": "Not found"}},
)

@router.get("/{employee_id}")
def get_report(employee_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    attendances = crud.get_attendances(db, employee_id)
    total_hours = sum((a.check_out - a.check_in).total_seconds() / 3600 for a in attendances if a.check_out)
    return {"employee_id": employee_id, "total_hours": total_hours}