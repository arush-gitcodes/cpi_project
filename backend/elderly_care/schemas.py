from pydantic import BaseModel, ConfigDict

from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

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
    model_config = ConfigDict(from_attributes=True)


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
    model_config = ConfigDict(from_attributes=True)


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
    model_config = ConfigDict(from_attributes=True)


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
    model_config = ConfigDict(from_attributes=True)

class EmergencyAlertBase(BaseModel):
    userID: int
    dateTime: datetime
    location: str
    resolved: bool

class EmergencyAlertCreate(EmergencyAlertBase):
    pass

class EmergencyAlert(EmergencyAlertBase):
    alertID: int
    model_config = ConfigDict(from_attributes=True)


class MessageBase(BaseModel):
    senderID: int
    receiverID: int
    content: str
    dateTime: datetime

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    messageID: int
    model_config = ConfigDict(from_attributes=True)


class VolunteerBase(BaseModel):
    name: str
    services: str
    availability: str

class VolunteerCreate(VolunteerBase):
    pass

class Volunteer(VolunteerBase):
    volunteerID: int
    model_config = ConfigDict(from_attributes=True)


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
    model_config = ConfigDict(from_attributes=True)


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
    model_config = ConfigDict(from_attributes=True)


class AlertBase(BaseModel):
    userID: int
    type: str
    dateTime: datetime
    details: str

class AlertCreate(AlertBase):
    pass

class Alert(AlertBase):
    alertID: int
    model_config = ConfigDict(from_attributes=True)
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
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
