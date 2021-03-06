from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class TokenData(BaseModel):
    client_email : Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str


class ClientLogin(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "email": "jdoe@example.com",
                "password": "password"
            }
        }


class Employee(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: EmailStr = Field(...)
    name: str = Field(...)
    status: str = Field(...)
    offer: float = Field(...)
    currency: str = Field(...)


class Client(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    address: str = Field(...)
    phone_number: str = Field(...)
    cin: Optional[str] = None
    tax_registration_number: Optional[str] = None
    employees: Optional[List[Employee]] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "facebook inc.",
                "email": "jdoe@facebook.com",
                "address": "1601 WILLOW ROAD MENLO PARK CA 94025",
                "phone_number": "+1 650-618-7714",
                "cin": "ADX687",
                "tax_registration_number": "TIN123456"
            }
        }

