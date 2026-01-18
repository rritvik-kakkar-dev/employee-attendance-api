# security.py
from datetime import datetime, timedelta, timezone
from typing import Optional, Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
import bcrypt
import hashlib

from config import get_settings
from schemas import TokenData
from database import get_db
from sqlalchemy.orm import Session

settings = get_settings()

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 1 day – adjust as needed


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Ensure hashed_password is bytes for bcrypt
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')
    
    # Pre-hash plain password to avoid 72 byte limit
    password_hash = hashlib.sha256(plain_password.encode('utf-8')).hexdigest().encode('utf-8')
    return bcrypt.checkpw(password_hash, hashed_password)

def get_password_hash(password: str) -> str:
    # Pre-hash password to avoid 72 byte limit
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest().encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_hash, salt).decode('utf-8')

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    if isinstance(encoded_jwt, bytes):
        return encoded_jwt.decode('utf-8')
    return encoded_jwt

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

async def get_current_user(
    token: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except jwt.PyJWTError:
        raise credentials_exception

    user = db.query(User).filter(User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user