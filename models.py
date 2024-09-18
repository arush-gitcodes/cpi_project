from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float,Text,ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class ElderlyUser(Base):
    __tablename__ = "elderlyusers"
    __table_args__ = {"schema": "elderlycare"}

    userID = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    healthConditions = Column(String)
    medications = Column(String)
    emergencyContacts = Column(String)
    profileImage = Column(String)
    address = Column(String)
    phoneNumber = Column(String)
    email = Column(String, unique=True, index=True)

class CaregiverFamilyMember(Base):
    __tablename__ = "caregiversfamilymembers"
    __table_args__ = {"schema": "elderlycare"}

    userID = Column(Integer, primary_key=True, index=True)
    elderlyUserID = Column(Integer, ForeignKey('elderlycare.elderlyusers.userID'))
    name = Column(String)
    relationship = Column(String)
    phoneNumber = Column(String)
    email = Column(String, unique=True, index=True)

class Reminder(Base):
    __tablename__ = "reminders"
    __table_args__ = {"schema": "elderlycare"}

    reminderID = Column(Integer, primary_key=True, index=True)
    userID = Column(Integer, ForeignKey('elderlycare.elderlyusers.userID'))
    type = Column(String)
    description = Column(String)
    dateTime = Column(DateTime)
    repeat = Column(String)
    status = Column(String)

class CheckIn(Base):
    __tablename__ = "checkins"
    __table_args__ = {"schema": "elderlycare"}

    checkInID = Column(Integer, primary_key=True, index=True)
    userID = Column(Integer, ForeignKey('elderlycare.elderlyusers.userID'))
    date = Column(DateTime)
    status = Column(String)
    mood = Column(String)
    healthStatus = Column(String)

class EmergencyAlert(Base):
    __tablename__ = "emergencyalerts"
    __table_args__ = {"schema": "elderlycare"}

    alertID = Column(Integer, primary_key=True, index=True)
    userID = Column(Integer, ForeignKey('elderlycare.elderlyusers.userID'))
    dateTime = Column(DateTime)
    location = Column(String)
    resolved = Column(Boolean)

class Message(Base):
    __tablename__ = "messages"
    __table_args__ = {"schema": "elderlycare"}

    messageID = Column(Integer, primary_key=True, index=True)
    senderID = Column(Integer, ForeignKey('elderlycare.elderlyusers.userID'))
    receiverID = Column(Integer, ForeignKey('elderlycare.elderlyusers.userID'))
    content = Column(String)
    dateTime = Column(DateTime)

class Volunteer(Base):
    __tablename__ = "volunteers"
    __table_args__ = {"schema": "elderlycare"}

    volunteerID = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    services = Column(String)
    availability = Column(String)

class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {"schema": "elderlycare"}

    taskID = Column(Integer, primary_key=True, index=True)
    userID = Column(Integer, ForeignKey('elderlycare.elderlyusers.userID'))
    description = Column(String)
    dueDate = Column(DateTime)
    status = Column(String)
    assignedTo = Column(Integer)

class HealthMetric(Base):
    __tablename__ = "healthmetrics"
    __table_args__ = {"schema": "elderlycare"}

    metricID = Column(Integer, primary_key=True, index=True)
    userID = Column(Integer, ForeignKey('elderlycare.elderlyusers.userID'))
    date = Column(DateTime)
    bloodPressure = Column(String)
    heartRate = Column(Integer)
    bloodSugar = Column(Float)

class Alert(Base):
    __tablename__ = "alerts"
    __table_args__ = {"schema": "elderlycare"}

    alertID = Column(Integer, primary_key=True, index=True)
    userID = Column(Integer, ForeignKey('elderlycare.elderlyusers.userID'))
    type = Column(String)
    dateTime = Column(DateTime)
    details = Column(String)

class Admin(Base):
    __tablename__ = "admin"
    __table_args__ = {"schema": "elderlycare"}

    adminID = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    phoneNumber = Column(String)

class DailyCheckIn(Base):
    __tablename__ = "daily_checkins"
    
    id = Column(Integer, primary_key=True, index=True)
    took_walk = Column(Boolean, default=False)
    did_physical_activity = Column(Boolean, default=False)
    step_count = Column(Integer, nullable=True)
    activity_duration = Column(Float, nullable=True)
    
    selected_mood = Column(String, nullable=True)
    feelings = Column(ARRAY(String), nullable=True)
    
    sleep_quality = Column(String, nullable=True)
    common_issues = Column(ARRAY(String), nullable=True)
    notes = Column(Text, nullable=True)
    
    meal_type = Column(String, nullable=True)
    meal_description = Column(Text, nullable=True)
    enjoyed_meal = Column(Boolean, default=False)
    good_appetite = Column(Boolean, default=False)
    enough_fluids = Column(Boolean, default=False)
    
    pain_areas = Column(ARRAY(String), nullable=True)