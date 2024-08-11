from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models

from . import crud
from . import schemas
from .database import engine, get_db
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ElderlyUser endpoints
@app.post("/elderly_users/", response_model=schemas.ElderlyUser)
def create_elderly_user(user: schemas.ElderlyUserCreate, db: Session = Depends(get_db)):
    return crud.create_elderly_user(db=db, user=user)

@app.get("/elderly_users/", response_model=List[schemas.ElderlyUser])
def read_elderly_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_elderly_users(db, skip=skip, limit=limit)
    return users

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
    caregivers = crud.get_caregivers(db, skip=skip, limit=limit)
    return caregivers

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
    reminders = crud.get_reminders(db, skip=skip, limit=limit)
    return reminders

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
    checkins = crud.get_checkins(db, skip=skip, limit=limit)
    return checkins

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
    alerts = crud.get_emergency_alerts(db, skip=skip, limit=limit)
    return alerts

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
    messages = crud.get_messages(db, skip=skip, limit=limit)
    return messages

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
    volunteers = crud.get_volunteers(db, skip=skip, limit=limit)
    return volunteers

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
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks

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
    health_metrics = crud.get_health_metrics(db, skip=skip, limit=limit)
    return health_metrics

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
    alerts = crud.get_alerts(db, skip=skip, limit=limit)
    return alerts

@app.get("/alerts/{alert_id}", response_model=schemas.Alert)
def read_alert(alert_id: int, db: Session = Depends(get_db)):
    db_alert = crud.get_alert(db, alert_id=alert_id)
    if db_alert is None:
        raise HTTPException(status_code=404, detail="Alert not found")
    return db_alert

@app.put("/alerts/{alert_id}", response_model=schemas.Alert)
def update_alert(alert_id: int, alert: schemas.AlertCreate, db: Session = Depends(get_db)):
    return crud.update_alert(db=db, alert_id=alert_id, alert=alert)

# Admin endpoints
@app.post("/admins/", response_model=schemas.Admin)
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    return crud.create_admin(db=db, admin=admin)

@app.get("/admins/", response_model=List[schemas.Admin])
def read_admins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    admins = crud.get_admins(db, skip=skip, limit=limit)
    return admins

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