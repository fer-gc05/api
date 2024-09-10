from fastapi import FastAPI, Depends, HTTPException
from routes.alarmRoutes import alarm_router
from routes.automationRoutes import automation_router
from routes.devicesRoutes import device_router
from routes.logsRoutes import logs_router
from routes.usersRoutes import user_router

app = FastAPI()

app.include_router(alarm_router)
app.include_router(automation_router)
app.include_router(device_router)
app.include_router(logs_router)
app.include_router(user_router)

@app.get("/", summary="API Root", description="FastAPI Root Endpoint")
def read_root():
    return {"message": "Welcome to the Alarm and Automation API!"}
