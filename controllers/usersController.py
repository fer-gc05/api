from fastapi import HTTPException, Depends, Header
from typing import Dict, Any, Optional
from datetime import datetime, timedelta
import jwt
import secrets

from models.usersModel import UserModel

SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

user_model = UserModel()
revoked_tokens = []

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(authorization: str) -> Dict[str, Any]:
    if authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    
    token = None
    parts = authorization.split()
    if len(parts) == 2 and parts[0].lower() == "bearer":
        token = parts[1]
    
    if token is None:
        raise HTTPException(status_code=401, detail="Token is missing")
    
    if token in revoked_tokens:
        raise HTTPException(status_code=401, detail="Token has been revoked")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"username": username}
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def login(username: str, password: str) -> Dict[str, Any]:
    if not username or not password:
        raise HTTPException(status_code=400, detail="Please fill in all fields")

    result = user_model.get_user_by_username_and_password(username, password)
    if 'error' in result:
        raise HTTPException(status_code=500, detail=result['error'])

    if result:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": username}, expires_delta=access_token_expires
        )
        return {"status": "success", "access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

def check_session(token: Dict[str, Any] = Depends(verify_token)) -> Dict[str, Any]:
    return {"status": "success", "username": token["username"]}

def create_user(username: str, password: str) -> Dict[str, Any]:
    if not username or not password:
        raise HTTPException(status_code=400, detail="Please fill in all fields for new user")

    existing_user = user_model.get_user_by_username(username)
    if existing_user:
        raise HTTPException(status_code=409, detail="User already exists")

    result = user_model.create_user(username, password)
    
    if isinstance(result, dict) and 'error' in result:
        raise HTTPException(status_code=500, detail=result['error'])
    elif not result:
        raise HTTPException(status_code=500, detail="Failed to create user")

    return {"status": "success"}

def delete_user(user_id: int) -> Dict[str, Any]:
    result = user_model.delete_user(user_id)

    if isinstance(result, dict) and 'error' in result:
        raise HTTPException(status_code=500, detail=result['error'])
    elif not result:
        raise HTTPException(status_code=500, detail="Failed to delete user")

    return {"status": "success"}

def logout(authorization: str = Header(None)) -> Dict[str, Any]:
    if authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    token_data = verify_token(authorization)
    revoked_tokens.append(token_data["username"])  # Store the username or token
    return {"status": "success"}

def assign_rfid_to_user(rfid_code: str, user_id: int, device_id: int) -> Dict[str, Any]:
    if not rfid_code or not user_id or not device_id:
        raise HTTPException(status_code=400, detail="Please provide all fields for RFID assignment")

    result = user_model.assign_rfid_to_user(rfid_code, user_id, device_id)
    if isinstance(result, dict) and 'error' in result:
        raise HTTPException(status_code=500, detail=result['error'])
    elif not result:  # `result` should be a boolean indicating success or failure
        raise HTTPException(status_code=500, detail="Failed to assign RFID")

    return {"status": "success"}


def desassign_rfid(user_id: int) -> Dict[str, Any]:
    if not user_id:
        raise HTTPException(status_code=400, detail="Please provide the user ID")

    result = user_model.desassign_rfid(user_id)
    if isinstance(result, dict) and 'error' in result:
        raise HTTPException(status_code=500, detail=result['error'])
    elif isinstance(result, bool) and not result:
        raise HTTPException(status_code=500, detail="Failed to desassign RFID")

    return {"status": "success", "message": "RFID desassigned successfully"}


def get_user_rfid() -> Dict[str, Any]:
    result = user_model.get_user_rfid()
    if 'error' in result:
        raise HTTPException(status_code=500, detail=result['error'])

    return {"status": "success", "data": result}

def set_rfid_mode(mode: str) -> Dict[str, Any]:
    if not mode:
        raise HTTPException(status_code=400, detail="Please provide the RFID mode")

    result = user_model.set_rfid_mode(mode)
    if isinstance(result, dict) and 'error' in result:
        raise HTTPException(status_code=500, detail=result['error'])
    elif isinstance(result, bool) and not result:
        raise HTTPException(status_code=500, detail="Failed to set RFID mode")

    return {"status": "success", "message": "RFID mode set successfully"}


def get_rfid_mode() -> Dict[str, Any]:
    result = user_model.get_rfid_mode()
    if 'error' in result:
        raise HTTPException(status_code=500, detail=result['error'])

    return result

def save_rfid_temp(rfid: str) -> Dict[str, Any]:
    if not rfid:
        raise HTTPException(status_code=400, detail="Please provide the RFID code")

    result = user_model.save_rfid_temp(rfid)
    
    if isinstance(result, dict) and 'error' in result:
        raise HTTPException(status_code=500, detail=result['error'])
    elif isinstance(result, bool) and not result:
        raise HTTPException(status_code=500, detail="Failed to save RFID temp data")

    return {"status": "success", "message": "RFID temp data saved successfully"}


def restart_rfid() -> Dict[str, Any]:
    result = user_model.restart_rfid_temp()

    if result:
        return {"status": "success", "message": "RFID temp reset successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to reset RFID temp")


def get_rfid_temp() -> Dict[str, Any]:
    result = user_model.get_rfid_temp()
    if result is None:
        raise HTTPException(status_code=500, detail="Error fetching RFID temp")

    return {"rfid_temp": result}

