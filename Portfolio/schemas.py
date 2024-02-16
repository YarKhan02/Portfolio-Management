from pydantic import BaseModel, EmailStr

from typing import Optional

from datetime import datetime


class PortfolioBase(BaseModel):
    owner_id: Optional[int] = None
    name: str
    amount: float
    price: Optional[float] = None
    coins: Optional[float] = None

class PortfolioAdded(PortfolioBase):
    created_at: datetime

    class Config:
        from_attributes = True

class PortfolioUpdated(PortfolioBase):
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class PortfolioResponse(BaseModel):
    name: str
    amount: float
    price: float
    coins: float

class NameCheck(BaseModel):
    name: str



# # Create User
# class UserCreate(BaseModel):
#     email: EmailStr
#     password: str


# Return create user response
# class UserResponse(BaseModel):
#     id: int
#     email: EmailStr
#     created_at: datetime

#     class Config:
#         from_attributes = True

# class User(BaseModel):
#     id: int
#     email: EmailStr

#     class Config:
#         from_attributes = True



# Token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None