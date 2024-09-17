
import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from fastapi import FastAPI, Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy.engine.base import Engine

from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import models
import crud
import schemas
from database import Base, get_db, engine
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

models.Base.metadata.create_all(bind=engine)

from database import Base, get_db, engine  # Import engine from database.py
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
models.Base.metadata.create_all(bind=engine)  # Use the imported engine instance

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#Security
SECRET_KEY = "BF319B2B37435"  # Replace with a real secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# Registration endpoint
@app.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# Login endpoint
@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Protected route example
@app.get("/users/me", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(get_current_user)):
    return current_user

# Security
SECRET_KEY = os.environ.get("SECRET_KEY", "BF319B2B37435")  # Use environment variable
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

@app.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(get_current_user)):
    return current_user

# ElderlyUser endpoints
@app.post("/elderly_users/", response_model=schemas.ElderlyUser)
def create_elderly_user(user: schemas.ElderlyUserCreate, db: Session = Depends(get_db)):
    return crud.create_elderly_user(db=db, user=user)

@app.get("/elderly_users/", response_model=List[schemas.ElderlyUser])
def read_elderly_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_elderly_users(db, skip=skip, limit=limit)

@app.get("/elderly_users/{user_id}", response_model=schemas.ElderlyUser)
def read_elderly_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_elderly_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/elderly_users/{user_id}", response_model=schemas.ElderlyUser)
def update_elderly_user(user_id: int, user: schemas.ElderlyUserCreate, db: Session = Depends(get_db)):
    return crud.update_elderly_user(db=db, user_id=user_id, user=user)

@app.delete("/elderly_users/{user_id}", response_model=schemas.ElderlyUser)
def delete_elderly_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_elderly_user(db=db, user_id=user_id)

# CaregiverFamilyMember endpoints
@app.post("/caregivers/", response_model=schemas.CaregiverFamilyMember)
def create_caregiver(caregiver: schemas.CaregiverFamilyMemberCreate, db: Session = Depends(get_db)):
    return crud.create_caregiver(db=db, caregiver=caregiver)

@app.get("/caregivers/", response_model=List[schemas.CaregiverFamilyMember])
def read_caregivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_caregivers(db, skip=skip, limit=limit)

@app.get("/caregivers/{caregiver_id}", response_model=schemas.CaregiverFamilyMember)
def read_caregiver(caregiver_id: int, db: Session = Depends(get_db)):
    db_caregiver = crud.get_caregiver(db, caregiver_id=caregiver_id)
    if db_caregiver is None:
        raise HTTPException(status_code=404, detail="Caregiver not found")
    return db_caregiver

@app.put("/caregivers/{caregiver_id}", response_model=schemas.CaregiverFamilyMember)
def update_caregiver(caregiver_id: int, caregiver: schemas.CaregiverFamilyMemberCreate, db: Session = Depends(get_db)):
    return crud.update_caregiver(db=db, caregiver_id=caregiver_id, caregiver=caregiver)

@app.delete("/caregivers/{caregiver_id}", response_model=schemas.CaregiverFamilyMember)
def delete_caregiver(caregiver_id: int, db: Session = Depends(get_db)):
    return crud.delete_caregiver(db=db, caregiver_id=caregiver_id)

# Reminder endpoints
@app.post("/reminders/", response_model=schemas.Reminder)
def create_reminder(reminder: schemas.ReminderCreate, db: Session = Depends(get_db)):
    return crud.create_reminder(db=db, reminder=reminder)

@app.get("/reminders/", response_model=List[schemas.Reminder])
def read_reminders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_reminders(db, skip=skip, limit=limit)

@app.get("/reminders/{reminder_id}", response_model=schemas.Reminder)
def read_reminder(reminder_id: int, db: Session = Depends(get_db)):
    db_reminder = crud.get_reminder(db, reminder_id=reminder_id)
    if db_reminder is None:
        raise HTTPException(status_code=404, detail="Reminder not found")
    return db_reminder

@app.put("/reminders/{reminder_id}", response_model=schemas.Reminder)
def update_reminder(reminder_id: int, reminder: schemas.ReminderCreate, db: Session = Depends(get_db)):
    return crud.update_reminder(db=db, reminder_id=reminder_id, reminder=reminder)

@app.delete("/reminders/{reminder_id}", response_model=schemas.Reminder)
def delete_reminder(reminder_id: int, db: Session = Depends(get_db)):
    return crud.delete_reminder(db=db, reminder_id=reminder_id)

# CheckIn endpoints
@app.post("/checkins/", response_model=schemas.CheckIn)
def create_checkin(checkin: schemas.CheckInCreate, db: Session = Depends(get_db)):
    return crud.create_checkin(db=db, checkin=checkin)

@app.get("/checkins/", response_model=List[schemas.CheckIn])
def read_checkins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_checkins(db, skip=skip, limit=limit)

@app.get("/checkins/{checkin_id}", response_model=schemas.CheckIn)
def read_checkin(checkin_id: int, db: Session = Depends(get_db)):
    db_checkin = crud.get_checkin(db, checkin_id=checkin_id)
    if db_checkin is None:
        raise HTTPException(status_code=404, detail="CheckIn not found")
    return db_checkin

@app.put("/checkins/{checkin_id}", response_model=schemas.CheckIn)
def update_checkin(checkin_id: int, checkin: schemas.CheckInCreate, db: Session = Depends(get_db)):
    return crud.update_checkin(db=db, checkin_id=checkin_id, checkin=checkin)

@app.delete("/checkins/{checkin_id}", response_model=schemas.CheckIn)
def delete_checkin(checkin_id: int, db: Session = Depends(get_db)):
    return crud.delete_checkin(db=db, checkin_id=checkin_id)

# EmergencyAlert endpoints
@app.post("/emergency_alerts/", response_model=schemas.EmergencyAlert)
def create_emergency_alert(alert: schemas.EmergencyAlertCreate, db: Session = Depends(get_db)):
    return crud.create_emergency_alert(db=db, alert=alert)

@app.get("/emergency_alerts/", response_model=List[schemas.EmergencyAlert])
def read_emergency_alerts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_emergency_alerts(db, skip=skip, limit=limit)

@app.get("/emergency_alerts/{alert_id}", response_model=schemas.EmergencyAlert)
def read_emergency_alert(alert_id: int, db: Session = Depends(get_db)):
    db_alert = crud.get_emergency_alert(db, alert_id=alert_id)
    if db_alert is None:
        raise HTTPException(status_code=404, detail="Emergency Alert not found")
    return db_alert

@app.put("/emergency_alerts/{alert_id}", response_model=schemas.EmergencyAlert)
def update_emergency_alert(alert_id: int, alert: schemas.EmergencyAlertCreate, db: Session = Depends(get_db)):
    return crud.update_emergency_alert(db=db, alert_id=alert_id, alert=alert)

@app.delete("/emergency_alerts/{alert_id}", response_model=schemas.EmergencyAlert)
def delete_emergency_alert(alert_id: int, db: Session = Depends(get_db)):
    return crud.delete_emergency_alert(db=db, alert_id=alert_id)

# Message endpoints
@app.post("/messages/", response_model=schemas.Message)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db=db, message=message)

@app.get("/messages/", response_model=List[schemas.Message])
def read_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_messages(db, skip=skip, limit=limit)

@app.get("/messages/{message_id}", response_model=schemas.Message)
def read_message(message_id: int, db: Session = Depends(get_db)):
    db_message = crud.get_message(db, message_id=message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message

@app.delete("/messages/{message_id}", response_model=schemas.Message)
def delete_message(message_id: int, db: Session = Depends(get_db)):
    return crud.delete_message(db=db, message_id=message_id)

# Volunteer endpoints
@app.post("/volunteers/", response_model=schemas.Volunteer)
def create_volunteer(volunteer: schemas.VolunteerCreate, db: Session = Depends(get_db)):
    return crud.create_volunteer(db=db, volunteer=volunteer)

@app.get("/volunteers/", response_model=List[schemas.Volunteer])
def read_volunteers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_volunteers(db, skip=skip, limit=limit)

@app.get("/volunteers/{volunteer_id}", response_model=schemas.Volunteer)
def read_volunteer(volunteer_id: int, db: Session = Depends(get_db)):
    db_volunteer = crud.get_volunteer(db, volunteer_id=volunteer_id)
    if db_volunteer is None:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    return db_volunteer

@app.put("/volunteers/{volunteer_id}", response_model=schemas.Volunteer)
def update_volunteer(volunteer_id: int, volunteer: schemas.VolunteerCreate, db: Session = Depends(get_db)):
    return crud.update_volunteer(db=db, volunteer_id=volunteer_id, volunteer=volunteer)

@app.delete("/volunteers/{volunteer_id}", response_model=schemas.Volunteer)
def delete_volunteer(volunteer_id: int, db: Session = Depends(get_db)):
    return crud.delete_volunteer(db=db, volunteer_id=volunteer_id)

# Task endpoints
@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@app.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tasks(db, skip=skip, limit=limit)
@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.update_task(db=db, task_id=task_id, task=task)

@app.delete("/tasks/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db=db, task_id=task_id)

# HealthMetric endpoints
@app.post("/health_metrics/", response_model=schemas.HealthMetric)
def create_health_metric(health_metric: schemas.HealthMetricCreate, db: Session = Depends(get_db)):
    return crud.create_health_metric(db=db, health_metric=health_metric)

@app.get("/health_metrics/", response_model=List[schemas.HealthMetric])
def read_health_metrics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_health_metrics(db, skip=skip, limit=limit)

@app.get("/health_metrics/{metric_id}", response_model=schemas.HealthMetric)
def read_health_metric(metric_id: int, db: Session = Depends(get_db)):
    db_health_metric = crud.get_health_metric(db, metric_id=metric_id)
    if db_health_metric is None:
        raise HTTPException(status_code=404, detail="Health Metric not found")
    return db_health_metric

@app.put("/health_metrics/{metric_id}", response_model=schemas.HealthMetric)
def update_health_metric(metric_id: int, health_metric: schemas.HealthMetricCreate, db: Session = Depends(get_db)):
    return crud.update_health_metric(db=db, metric_id=metric_id, health_metric=health_metric)

@app.delete("/health_metrics/{metric_id}", response_model=schemas.HealthMetric)
def delete_health_metric(metric_id: int, db: Session = Depends(get_db)):
    return crud.delete_health_metric(db=db, metric_id=metric_id)

# Alert endpoints
@app.post("/alerts/", response_model=schemas.Alert)
def create_alert(alert: schemas.AlertCreate, db: Session = Depends(get_db)):
    return crud.create_alert(db=db, alert=alert)

@app.get("/alerts/", response_model=List[schemas.Alert])
def read_alerts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_alerts(db, skip=skip, limit=limit)

@app.get("/alerts/{alert_id}", response_model=schemas.Alert)
def read_alert(alert_id: int, db: Session = Depends(get_db)):
    db_alert = crud.get_alert(db, alert_id=alert_id)
    if db_alert is None:
        raise HTTPException(status_code=404, detail="Alert not found")
    return db_alert

@app.put("/alerts/{alert_id}", response_model=schemas.Alert)
def update_alert(alert_id: int, alert: schemas.AlertCreate, db: Session = Depends(get_db)):
    return crud.update_alert(db=db, alert_id=alert_id, alert=alert)

@app.delete("/alerts/{alert_id}", response_model=schemas.Alert)
def delete_alert(alert_id: int, db: Session = Depends(get_db)):
    return crud.delete_alert(db=db, alert_id=alert_id)

# Admin endpoints
@app.post("/admins/", response_model=schemas.Admin)
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    return crud.create_admin(db=db, admin=admin)

@app.get("/admins/", response_model=List[schemas.Admin])
def read_admins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_admins(db, skip=skip, limit=limit)

@app.get("/admins/{admin_id}", response_model=schemas.Admin)
def read_admin(admin_id: int, db: Session = Depends(get_db)):
    db_admin = crud.get_admin(db, admin_id=admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return db_admin

@app.put("/admins/{admin_id}", response_model=schemas.Admin)
def update_admin(admin_id: int, admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    return crud.update_admin(db=db, admin_id=admin_id, admin=admin)

@app.delete("/admins/{admin_id}", response_model=schemas.Admin)
def delete_admin(admin_id: int, db: Session = Depends(get_db)):
    return crud.delete_admin(db=db, admin_id=admin_id)

# Create the database tables on startup
@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(bind=engine)

# Daily Check-In endpoints
@app.post("/daily_checkin/", response_model=schemas.DailyCheckInResponse)
def create_daily_checkin(checkin_data: schemas.DailyCheckInRequest, db: Session = Depends(get_db)):
    return crud.create_daily_checkin(db, checkin_data)

@app.get("/daily_checkins/", response_model=List[schemas.DailyCheckInResponse])
def read_daily_checkins(db: Session = Depends(get_db)):
    return crud.get_daily_checkins(db)

@app.get("/daily_checkin/{checkin_id}", response_model=schemas.DailyCheckInResponse)
def read_daily_checkin(checkin_id: int, db: Session = Depends(get_db)):
    checkin = crud.get_daily_checkin_by_id(db, checkin_id)
    if checkin is None:
        raise HTTPException(status_code=404, detail="Daily check-in not found")
    return checkin

@app.put("/daily_checkin/{checkin_id}", response_model=schemas.DailyCheckInResponse)
def update_daily_checkin(checkin_id: int, checkin_data: schemas.DailyCheckInRequest, db: Session = Depends(get_db)):
    return crud.update_daily_checkin(db, checkin_id, checkin_data)

@app.delete("/daily_checkin/{checkin_id}")
def delete_daily_checkin(checkin_id: int, db: Session = Depends(get_db)):
    crud.delete_daily_checkin(db, checkin_id)
    return {"message": "Daily check-in deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)