from pydantic import BaseModel
from datetime import date, datetime

class EmployeeBase(BaseModel):
    name: str
    email: str
    position: str
    doj: date | None = None

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True


class AttendanceBase(BaseModel):
    employee_id: int
    check_in: datetime | None = None
    check_out: datetime | None = None

class AttendanceCreate(AttendanceBase):
    pass

class Attendance(AttendanceBase):
    id: int

    class Config:
        from_attributes = True