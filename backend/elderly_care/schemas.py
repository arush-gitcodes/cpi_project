from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ElderlyUserBase(BaseModel):
    name: str
    age: int
    healthConditions: Optional[str] = None
    medications: Optional[str] = None
    emergencyContacts: Optional[str] = None
    profileImage: Optional[str] = None
    address: str
    phoneNumber: str
    email: str

class ElderlyUserCreate(ElderlyUserBase):
    pass

class ElderlyUser(ElderlyUserBase):
    userID: int

    class Config:
        orm_mode = True

class CaregiverFamilyMemberBase(BaseModel):
    elderlyUserID: int
    name: str
    relationship: str
    phoneNumber: str
    email: str

class CaregiverFamilyMemberCreate(CaregiverFamilyMemberBase):
    pass

class CaregiverFamilyMember(CaregiverFamilyMemberBase):
    userID: int

    class Config:
        orm_mode = True

class ReminderBase(BaseModel):
    userID: int
    type: str
    description: str
    dateTime: datetime
    repeat: str
    status: str

class ReminderCreate(ReminderBase):
    pass

class Reminder(ReminderBase):
    reminderID: int

    class Config:
        orm_mode = True

class CheckInBase(BaseModel):
    userID: int
    date: datetime
    status: str
    mood: str
    healthStatus: str

class CheckInCreate(CheckInBase):
    pass

class CheckIn(CheckInBase):
    checkInID: int

    class Config:
        orm_mode = True

class EmergencyAlertBase(BaseModel):
    userID: int
    dateTime: datetime
    location: str
    resolved: bool

class EmergencyAlertCreate(EmergencyAlertBase):
    pass

class EmergencyAlert(EmergencyAlertBase):
    alertID: int

    class Config:
        orm_mode = True

class MessageBase(BaseModel):
    senderID: int
    receiverID: int
    content: str
    dateTime: datetime

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    messageID: int

    class Config:
        orm_mode = True

class VolunteerBase(BaseModel):
    name: str
    services: str
    availability: str

class VolunteerCreate(VolunteerBase):
    pass

class Volunteer(VolunteerBase):
    volunteerID: int

    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    userID: int
    description: str
    dueDate: datetime
    status: str
    assignedTo: int

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    taskID: int

    class Config:
        orm_mode = True

class HealthMetricBase(BaseModel):
    userID: int
    date: datetime
    bloodPressure: str
    heartRate: int
    bloodSugar: float

class HealthMetricCreate(HealthMetricBase):
    pass

class HealthMetric(HealthMetricBase):
    metricID: int

    class Config:
        orm_mode = True

class AlertBase(BaseModel):
    userID: int
    type: str
    dateTime: datetime
    details: str

class AlertCreate(AlertBase):
    pass

class Alert(AlertBase):
    alertID: int

    class Config:
        orm_mode = True

class AdminBase(BaseModel):
    name: str
    email: str
    phoneNumber: str

class AdminCreate(AdminBase):
    pass

class Admin(AdminBase):
    adminID: int

    class Config:
        orm_mode = True