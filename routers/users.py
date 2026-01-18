from fastapi import APIRouter
from sqlalchemy.orm import Session
from database import get_db
import crud
import schemas
from fastapi import Depends, HTTPException
from config import get_settings, Settings
from fastapi.middleware.cors import CORSMiddleware
from routers import auth
from security import get_current_user
from models import User

router = APIRouter(
    prefix="/users",
    tags=["Users"],          # ← This creates the group
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.create_user(db, user)

@router.get("/{user_id}", response_model=schemas.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = crud.get_user_by_email(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user