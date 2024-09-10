from fastapi import APIRouter, Depends
from controllers.usersController import (
    login,
    check_session,
    create_user,
    delete_user,
    logout,
    assign_rfid_to_user,
    desassign_rfid,
    get_user_rfid,
    set_rfid_mode,
    get_rfid_mode,
    save_rfid_temp,
    restart_rfid,
    get_rfid_temp,
)

user_router = APIRouter()

@user_router.post("/user/login", summary="User Login")
def user_login(username: str, password: str):
    return login(username, password)

@user_router.get("/user/session", summary="Check User Session")
def check_user_session(token: dict = Depends(check_session)):
    return token

@user_router.post("/user/create", summary="Create New User")
def create_new_user(username: str, password: str):
    return create_user(username, password)

@user_router.delete("/user/{user_id}", summary="Delete User")
def remove_user(user_id: int):
    return delete_user(user_id)

@user_router.post("/user/logout", summary="User Logout")
def user_logout():
    return logout()

@user_router.post("/user/assign-rfid", summary="Assign RFID to User")
def assign_rfid(rfid_code: str, user_id: int, device_id: int):
    return assign_rfid_to_user(rfid_code, user_id, device_id)

@user_router.post("/user/desassign-rfid", summary="Desassign RFID from User")
def desassign_user_rfid(user_id: int):
    return desassign_rfid(user_id)

@user_router.get("/user/list-rfid", summary="List User RFID")
def list_user_rfid():
    return get_user_rfid()

@user_router.post("/user/set-rfid-mode", summary="Set RFID Mode")
def set_rfid_reading_mode(mode: str):
    return set_rfid_mode(mode)

@user_router.get("/user/get-rfid-mode", summary="Get RFID Mode")
def get_rfid_reading_mode():
    return get_rfid_mode()

@user_router.post("/user/save-rfid-temp", summary="Save RFID Temp Data")
def save_rfid_temp_data(rfid: str):
    return save_rfid_temp(rfid)

@user_router.post("/user/restart-rfid", summary="Restart RFID Temp")
def restart_rfid_temp():
    return restart_rfid()

@user_router.get("/user/get-rfid-temp", summary="Get RFID Temp Data")
def get_rfid_temp_data():
    return get_rfid_temp()
