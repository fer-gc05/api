from fastapi import APIRouter
from controllers.automationController import AutomationController

automation_router = APIRouter()
automation_controller = AutomationController()

@automation_router.post("/automation/activate", summary="Activate Automation")
def activate_automation():
    return automation_controller.activate_automation()

@automation_router.post("/automation/deactivate", summary="Deactivate Automation")
def deactivate_automation():
    return automation_controller.deactivate_automation()

@automation_router.post("/automation/configure", summary="Update Automation Configuration")
def update_automation_configuration(turn_on_hour: str, turn_off_hour: str):
    return automation_controller.update_automation_configuration(turn_on_hour, turn_off_hour)

@automation_router.get("/automation/status", summary="Get Automation Status")
def get_automation_status():
    return automation_controller.get_automation_status()

@automation_router.get("/automation/check", summary="Check Automation")
def check_automation():
    return automation_controller.check_automation()
