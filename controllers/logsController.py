from fastapi import HTTPException
from models.logsModel import LogModel
from typing import Optional, List, Dict, Any

log_model = LogModel()

def get_alarm_logs(start_time: Optional[str] = None, end_time: Optional[str] = None, search: Optional[str] = None) -> List[Dict[str, Any]]:
    result = log_model.get_alarm_logs(start_time, end_time, search)
    if 'error' in result:
        raise HTTPException(status_code=500, detail=result['error'])
    return result

def get_detection_logs(start_time: Optional[str] = None, end_time: Optional[str] = None) -> List[Dict[str, Any]]:
    result = log_model.get_detection_logs(start_time, end_time)
    if 'error' in result:
        raise HTTPException(status_code=500, detail=result['error'])
    return result
