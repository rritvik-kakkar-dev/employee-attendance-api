
from security import create_access_token
from datetime import timedelta
import jwt

try:
    token = create_access_token(data={"sub": "test@example.com"}, expires_delta=timedelta(minutes=10))
    print("Token created successfully")
    print("Token:", token)
    if isinstance(token, bytes):
        print("Warning: Token is bytes, expected str")
except Exception as e:
    print("Error:", e)
    import traceback
    traceback.print_exc()
