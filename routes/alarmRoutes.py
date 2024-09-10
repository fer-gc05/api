from fastapi import APIRouter, HTTPException
from controllers.alarmController import (
    check_alarm_status,
    toggle_alarm,
    turn_on_alarm,
    turn_off_alarm,
    intruder_detected,
)

alarm_router = APIRouter()

@alarm_router.get("/alarm/status/{alarm_id}", summary="Get Alarm Status", response_model=dict)
def get_alarm_status(alarm_id: int):
    status = check_alarm_status(alarm_id)
    if status is None:
        raise HTTPException(status_code=404, detail="Alarm not found")
    return status

@alarm_router.post("/alarm/toggle/{rfid}", summary="Toggle Alarm Status")
def toggle_alarm_status(rfid: str):
    return toggle_alarm(rfid)

@alarm_router.post("/alarm/on", summary="Turn On Alarm")
def activate_alarm(password: str):
    return turn_on_alarm(password)

@alarm_router.post("/alarm/off", summary="Turn Off Alarm")
def deactivate_alarm(password: str):
    return turn_off_alarm(password)

@alarm_router.post("/alarm/intruder-detected", summary="Handle Intruder Detection")
def handle_intruder_detection():
    return intruder_detected()
