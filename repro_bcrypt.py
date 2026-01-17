
from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash_original(password: str) -> str:
    return pwd_context.hash(password)

def get_password_hash_fixed(password: str) -> str:
    print(f"Original password length: {len(password)}")
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    print(f"SHA256 hash length: {len(password_hash)}")
    print(f"SHA256 hash: {password_hash}")
    return pwd_context.hash(password_hash)

long_password = "a" * 80

print("--- Testing Fixed Method ---")
try:
    hashed = get_password_hash_fixed(long_password)
    print("Success! Hash:", hashed)
except Exception as e:
    print("Failed with:", e)

import bcrypt
print("\n--- Testing Direct Bcrypt ---")
try:
    pw = b"a" * 64
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pw, salt)
    print("Success with 64 bytes! Hash:", hashed)
    
    pw = b"a" * 73
    hashed = bcrypt.hashpw(pw, salt)
    print("Success with 73 bytes! Hash:", hashed)
except Exception as e:
    print("Failed with:", e)
