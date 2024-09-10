from fastapi import HTTPException
from models.automationModel import AutomationModel
from datetime import datetime

class AutomationController:
    def __init__(self):
        self.model = AutomationModel()

    def activate_automation(self):
        response = self.model.update_automation_status(1)
        return {'message': 'Automation activated'}

    def deactivate_automation(self):
        response = self.model.update_automation_status(0)
        return {'message': 'Automation deactivated'}

    def update_automation_configuration(self, turn_on_hour: str, turn_off_hour: str):
        turn_on_hour = datetime.strptime(turn_on_hour, '%H:%M').strftime('%H:%M')
        turn_off_hour = datetime.strptime(turn_off_hour, '%H:%M').strftime('%H:%M')
        response = self.model.update_automation_configuration(turn_on_hour, turn_off_hour)
        return response

    def get_automation_status(self):
        response = self.model.get_automation_status()
        return response

    def check_automation(self):
        data = self.model.get_automation_and_device_status()
        if 'message' in data:
            raise HTTPException(status_code=404, detail=data['message'])

        status = data.get('automation_status')
        turn_on_hour = data.get('turnOnHour')
        turn_off_hour = data.get('turnOffHour')
        current_time = datetime.now().strftime('%H:%M')
        current_device_status = data.get('device_status')

        
        def format_time(value):
            if isinstance(value, str):
                try:
                    datetime.strptime(value, '%H:%M')
                    return value
                except ValueError:
                    return 'Invalid time format'
            return 'No time set'

        turn_on_hour = format_time(turn_on_hour)
        turn_off_hour = format_time(turn_off_hour)

        if status == 1:
            if current_time == turn_on_hour:
                return self.update_device_status(current_device_status, 1, "Alarma activada por automatización")
            elif current_time == turn_off_hour:
                self.model.update_automation_status(0)
                return self.update_device_status(current_device_status, 0, "Alarma desactivada por automatización")

        return {'message': 'Automation process completed'}


    def update_device_status(self, current_device_status: int, new_status: int, log_message: str):
        if current_device_status != new_status:
            response = self.model.update_device_status(new_status)
            if response['message'] == 'Device status updated':
                return self.model.log_alarm_action(1, log_message)
            else:
                raise HTTPException(status_code=500, detail='Error updating device status')
        return {'message': 'Device status unchanged'}
