from fastapi import HTTPException
from models.deviceModel import DeviceModel

device_model = DeviceModel()

def check_password(password: str):
    device = device_model.get_device_by_id(1)
    if 'error' in device:
        raise HTTPException(status_code=404, detail=device['error'])
    
    if password == device.get('activationPassword'):
        return {'status': 'success', 'message': 'Password correct'}
    else:
        return {'status': 'error', 'message': 'Password incorrect'}

def update_password(current_password: str, new_password: str):
    result = device_model.get_activation_password(1)
    if 'error' in result:
        raise HTTPException(status_code=404, detail=result['error'])
    
    stored_password = result.get('activationPassword')
    if current_password == stored_password:
        update_result = device_model.update_activation_password(1, new_password)
        if 'error' in update_result:
            raise HTTPException(status_code=500, detail=update_result['error'])
        return {'status': 'success', 'message': 'Password updated successfully'}
    else:
        return {'status': 'error', 'message': 'The current password is incorrect'}
