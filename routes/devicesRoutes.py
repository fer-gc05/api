from fastapi import APIRouter
from controllers.deviceController import check_password, update_password

device_router = APIRouter()

@device_router.post("/device/check-password", summary="Check Device Password")
def verify_password(password: str):
    return check_password(password)

@device_router.put("/device/update-password", summary="Update Device Password")
def change_password(current_password: str, new_password: str):
    return update_password(current_password, new_password)
