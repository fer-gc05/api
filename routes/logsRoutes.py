from fastapi import APIRouter, Query
from controllers.logsController import get_alarm_logs, get_detection_logs

logs_router = APIRouter()

@logs_router.get("/logs/alarm", summary="Fetch Alarm Logs")
def fetch_alarm_logs(
    start_time: str = Query(None), 
    end_time: str = Query(None), 
    search: str = Query(None)
):
    return get_alarm_logs(start_time, end_time, search)

@logs_router.get("/logs/detection", summary="Fetch Detection Logs")
def fetch_detection_logs(
    start_time: str = Query(None), 
    end_time: str = Query(None)
):
    return get_detection_logs(start_time, end_time)
