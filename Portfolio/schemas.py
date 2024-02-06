from pydantic import BaseModel, EmailStr

from typing import Optional

from datetime import datetime


class TokenValidity(BaseModel):
    name: str
    amount: float


class PortfolioBase(BaseModel):
    name: str
    amount: float
    price: float


class PortfolioResponse(BaseModel):
    id: int
    name: str
    price: float
    created_at: datetime