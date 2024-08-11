from sqlalchemy.orm import Session

from . import models
from . import schemas
from datetime import datetime

# ElderlyUser CRUD operations
def create_elderly_user(db: Session, user: schemas.ElderlyUserCreate):
    db_user = models.ElderlyUser(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_elderly_user(db: Session, user_id: int):
    return db.query(models.ElderlyUser).filter(models.ElderlyUser.userID == user_id).first()

def get_elderly_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ElderlyUser).offset(skip).limit(limit).all()

def update_elderly_user(db: Session, user_id: int, user: schemas.ElderlyUserCreate):
    db_user = db.query(models.ElderlyUser).filter(models.ElderlyUser.userID == user_id).first()
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_elderly_user(db: Session, user_id: int):
    db_user = db.query(models.ElderlyUser).filter(models.ElderlyUser.userID == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user

# CaregiverFamilyMember CRUD operations
def create_caregiver(db: Session, caregiver: schemas.CaregiverFamilyMemberCreate):
    db_caregiver = models.CaregiverFamilyMember(**caregiver.dict())
    db.add(db_caregiver)
    db.commit()
    db.refresh(db_caregiver)
    return db_caregiver

def get_caregiver(db: Session, caregiver_id: int):
    return db.query(models.CaregiverFamilyMember).filter(models.CaregiverFamilyMember.userID == caregiver_id).first()

def get_caregivers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CaregiverFamilyMember).offset(skip).limit(limit).all()

def update_caregiver(db: Session, caregiver_id: int, caregiver: schemas.CaregiverFamilyMemberCreate):
    db_caregiver = db.query(models.CaregiverFamilyMember).filter(models.CaregiverFamilyMember.userID == caregiver_id).first()
    for key, value in caregiver.dict().items():
        setattr(db_caregiver, key, value)
    db.commit()
    db.refresh(db_caregiver)
    return db_caregiver

def delete_caregiver(db: Session, caregiver_id: int):
    db_caregiver = db.query(models.CaregiverFamilyMember).filter(models.CaregiverFamilyMember.userID == caregiver_id).first()
    db.delete(db_caregiver)
    db.commit()
    return db_caregiver

# Reminder CRUD operations
def create_reminder(db: Session, reminder: schemas.ReminderCreate):
    db_reminder = models.Reminder(**reminder.dict())
    db.add(db_reminder)
    db.commit()
    db.refresh(db_reminder)
    return db_reminder

def get_reminder(db: Session, reminder_id: int):
    return db.query(models.Reminder).filter(models.Reminder.reminderID == reminder_id).first()

def get_reminders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reminder).offset(skip).limit(limit).all()

def update_reminder(db: Session, reminder_id: int, reminder: schemas.ReminderCreate):
    db_reminder = db.query(models.Reminder).filter(models.Reminder.reminderID == reminder_id).first()
    for key, value in reminder.dict().items():
        setattr(db_reminder, key, value)
    db.commit()
    db.refresh(db_reminder)
    return db_reminder

def delete_reminder(db: Session, reminder_id: int):
    db_reminder = db.query(models.Reminder).filter(models.Reminder.reminderID == reminder_id).first()
    db.delete(db_reminder)
    db.commit()
    return db_reminder

# CheckIn CRUD operations
def create_checkin(db: Session, checkin: schemas.CheckInCreate):
    db_checkin = models.CheckIn(**checkin.dict())
    db.add(db_checkin)
    db.commit()
    db.refresh(db_checkin)
    return db_checkin

def get_checkin(db: Session, checkin_id: int):
    return db.query(models.CheckIn).filter(models.CheckIn.checkInID == checkin_id).first()

def get_checkins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CheckIn).offset(skip).limit(limit).all()

def update_checkin(db: Session, checkin_id: int, checkin: schemas.CheckInCreate):
    db_checkin = db.query(models.CheckIn).filter(models.CheckIn.checkInID == checkin_id).first()
    for key, value in checkin.dict().items():
        setattr(db_checkin, key, value)
    db.commit()
    db.refresh(db_checkin)
    return db_checkin

def delete_checkin(db: Session, checkin_id: int):
    db_checkin = db.query(models.CheckIn).filter(models.CheckIn.checkInID == checkin_id).first()
    db.delete(db_checkin)
    db.commit()
    return db_checkin

# EmergencyAlert CRUD operations
def create_emergency_alert(db: Session, alert: schemas.EmergencyAlertCreate):
    db_alert = models.EmergencyAlert(**alert.dict())
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert

def get_emergency_alert(db: Session, alert_id: int):
    return db.query(models.EmergencyAlert).filter(models.EmergencyAlert.alertID == alert_id).first()

def get_emergency_alerts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.EmergencyAlert).offset(skip).limit(limit).all()

def update_emergency_alert(db: Session, alert_id: int, alert: schemas.EmergencyAlertCreate):
    db_alert = db.query(models.EmergencyAlert).filter(models.EmergencyAlert.alertID == alert_id).first()
    for key, value in alert.dict().items():
        setattr(db_alert, key, value)
    db.commit()
    db.refresh(db_alert)
    return db_alert

def delete_emergency_alert(db: Session, alert_id: int):
    db_alert = db.query(models.EmergencyAlert).filter(models.EmergencyAlert.alertID == alert_id).first()
    db.delete(db_alert)
    db.commit()
    return db_alert

# Implement similar CRUD operations for Message, Volunteer, Task, HealthMetric, Alert, and Admin models