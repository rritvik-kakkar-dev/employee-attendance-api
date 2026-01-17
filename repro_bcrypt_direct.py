
import bcrypt
import hashlib

def get_password_hash(password: str) -> str:
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest().encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_hash, salt).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')
    password_hash = hashlib.sha256(plain_password.encode('utf-8')).hexdigest().encode('utf-8')
    return bcrypt.checkpw(password_hash, hashed_password)

long_password = "a" * 80
print(f"Testing password length: {len(long_password)}")

try:
    hashed = get_password_hash(long_password)
    print("Hashing success! Hash:", hashed)
    
    is_valid = verify_password(long_password, hashed)
    print("Verification success:", is_valid)
    
    is_invalid = verify_password("wrong", hashed)
    print("Invalid check success:", is_invalid is False)
    
except Exception as e:
    print("Failed with:", e)
