from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
from pydantic.networks import EmailStr

# ── Employee ────────────────────────────────────────────────

class EmployeeBase(BaseModel):
    name: str
    email: str
    position: str
    doj: date | None = None
    phone: Optional[str] = None
    department: Optional[str] = None
    status: Optional[str] = None
    manager_id: Optional[int] = None

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True


# ── Attendance ────────────────────────────────────────────────

class AttendanceBase(BaseModel):
    employee_id: int
    check_in: datetime | None = None
    check_out: datetime | None = None
    status: Optional[str] = None
    notes: Optional[str] = None

class AttendanceCreate(AttendanceBase):
    pass

class Attendance(AttendanceBase):
    id: int

    class Config:
        from_attributes = True


# ── User ────────────────────────────────────────────────

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    updated_at: Optional[datetime] = None
    last_login_at: Optional[datetime] = None
    password_changed_at: Optional[datetime] = None

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

# ── Token ───────────────────────────────────────────────

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    email: Optional[str] = None