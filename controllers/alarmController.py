from fastapi import HTTPException
from models.alarmModel import AlarmModel

alarm_model = AlarmModel()

def check_alarm_status(alarm_id: int):
    result = alarm_model.get_alarm_status(alarm_id)
    if 'error' in result:
        raise HTTPException(status_code=404, detail=result['error'])
    return result

def toggle_alarm(rfid: str):
    result = alarm_model.get_device_by_rfid(rfid)
    if result is None:
        raise HTTPException(status_code=404, detail="No device found")
    
    alarm_id = result['device_id']
    status = alarm_model.get_alarm_status(alarm_id)
    if 'error' in status:
        raise HTTPException(status_code=404, detail=status['error'])
    
    current_status = status['status']
    new_status = 0 if current_status == 'Alarm activated' else 1

    update_result = alarm_model.update_alarm_status(alarm_id, new_status)
    if 'error' in update_result:
        raise HTTPException(status_code=500, detail=update_result['error'])
    
    message = 'Alarm activated' if new_status == 1 else 'Alarm deactivated'
    action = f'Alarma activada por {result["username"]}' if new_status == 1 else f'Alarma desactivada por {result["username"]}'
    
    alarm_model.insert_alarm_log(alarm_id, action)
    
    if new_status == 0:
        deactivate_automation(alarm_id)

    return {'success': message}

def turn_on_alarm(password: str):
    result = alarm_model.get_alarm_status(1)
    if 'error' in result:
        raise HTTPException(status_code=404, detail=result['error'])
    
    if result['status'] == 'Alarm deactivated':
        if password == result['activationPassword']:
            update_result = alarm_model.update_alarm_status(1, 1)
            if 'success' in update_result:
                alarm_model.insert_alarm_log(1, 'Alarma activada por interfaz web')
                return {'message': 'Alarm activated'}
            else:
                raise HTTPException(status_code=500, detail='Error activating alarm')
        else:
            raise HTTPException(status_code=400, detail='Incorrect password')
    else:
        return {'message': 'Alarm already activated'}

def turn_off_alarm(password: str):
    result = alarm_model.get_alarm_status(1)
    if 'error' in result:
        raise HTTPException(status_code=404, detail=result['error'])
    
    if result['status'] == 'Alarm activated':
        if password == result['activationPassword']:
            update_result = alarm_model.update_alarm_status(1, 0)
            if 'success' in update_result:
                alarm_model.insert_alarm_log(1, 'Alarma desactivada por interfaz web')
                deactivate_automation(1)
                return {'message': 'Alarm deactivated'}
            else:
                raise HTTPException(status_code=500, detail='Error deactivating alarm')
        else:
            raise HTTPException(status_code=400, detail='Incorrect password')
    else:
        return {'message': 'Alarm already deactivated'}

def intruder_detected():
    result = alarm_model.insert_detection_log(1, 'Intruso detectado')
    if 'success' in result:
        return {'message': 'Detection log inserted'}
    else:
        raise HTTPException(status_code=500, detail=result['error'])

def deactivate_automation(alarm_id: int):
    result = alarm_model.get_automation_status(alarm_id)
    if 'error' in result:
        raise HTTPException(status_code=404, detail=result['error'])
    
    if result['status'] == 1:
        update_result = alarm_model.update_automation_status(alarm_id, 0)
        if 'success' not in update_result:
            raise HTTPException(status_code=500, detail='Error deactivating automation')