from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud
import schemas
from config import get_settings, Settings
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, employees, attendances, reports, users
from security import get_current_user
from models import User

app = FastAPI(title="Employee & Attendance API")

app.include_router(auth.router)
app.include_router(employees.router)
app.include_router(attendances.router)
app.include_router(reports.router)
app.include_router(users.router)
