from pydantic import BaseModel, EmailStr

from typing import Optional

from datetime import datetime


class TokenValidity(BaseModel):
    id: Optional[int] = None
    name: str
    amount: float
    price: Optional[float] = None
    coins: Optional[float] = None
    created_at: Optional[datetime] = None



class PortfolioBase(BaseModel):
    name: str
    amount: float
    price: float
    coins: float


class NameCheck(BaseModel):
    name: str