from sqlalchemy.orm import Session
import models
import schemas
from passlib.context import CryptContext
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user
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


def create_checkin(db: Session, checkin_data: schemas.DailyCheckInRequest):
    checkin = models.DailyCheckIn(
        took_walk=checkin_data.activity_tracking.took_walk,
        did_physical_activity=checkin_data.activity_tracking.did_physical_activity,
        step_count=checkin_data.activity_tracking.step_count,
        activity_duration=checkin_data.activity_tracking.activity_duration,
        selected_mood=checkin_data.mood_tracking.selected_mood,
        feelings=checkin_data.mood_tracking.feelings,
        sleep_quality=checkin_data.sleep_tracking.sleep_quality,
        common_issues=checkin_data.sleep_tracking.common_issues,
        notes=checkin_data.sleep_tracking.notes,
        meal_type=checkin_data.meal_logging.meal_type,
        meal_description=checkin_data.meal_logging.meal_description,
        enjoyed_meal=checkin_data.meal_logging.enjoyed_meal,
        good_appetite=checkin_data.meal_logging.good_appetite,
        enough_fluids=checkin_data.meal_logging.enough_fluids,
        pain_areas=checkin_data.pain_tracking.pain_areas
    )
    db.add(checkin)
    db.commit()
    db.refresh(checkin)
    return checkin

def get_checkins(db: Session):
    return db.query(models.DailyCheckIn).all()

def get_checkin_by_id(db: Session, checkin_id: int):
    return db.query(models.DailyCheckIn).filter(models.DailyCheckIn.id == checkin_id).first()

def update_checkin(db: Session, checkin_id: int, checkin_data: schemas.DailyCheckInRequest):
    checkin = db.query(models.DailyCheckIn).filter(models.DailyCheckIn.id == checkin_id).first()
    
    if checkin:
        checkin.took_walk = checkin_data.activity_tracking.took_walk
        checkin.did_physical_activity = checkin_data.activity_tracking.did_physical_activity
        checkin.step_count = checkin_data.activity_tracking.step_count
        checkin.activity_duration = checkin_data.activity_tracking.activity_duration
        checkin.selected_mood = checkin_data.mood_tracking.selected_mood
        checkin.feelings = checkin_data.mood_tracking.feelings
        checkin.sleep_quality = checkin_data.sleep_tracking.sleep_quality
        checkin.common_issues = checkin_data.sleep_tracking.common_issues
        checkin.notes = checkin_data.sleep_tracking.notes
        checkin.meal_type = checkin_data.meal_logging.meal_type
        checkin.meal_description = checkin_data.meal_logging.meal_description
        checkin.enjoyed_meal = checkin_data.meal_logging.enjoyed_meal
        checkin.good_appetite = checkin_data.meal_logging.good_appetite
        checkin.enough_fluids = checkin_data.meal_logging.enough_fluids
        checkin.pain_areas = checkin_data.pain_tracking.pain_areas
        
        db.commit()
        db.refresh(checkin)
        
    return checkin

def delete_checkin(db: Session, checkin_id: int):
    checkin = db.query(models.DailyCheckIn).filter(models.DailyCheckIn.id == checkin_id).first()
    if checkin:
        db.delete(checkin)
        db.commit()
    return checkin
