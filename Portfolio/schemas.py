from pydantic import BaseModel, EmailStr

from typing import Optional

from datetime import datetime


class TokenValidity(BaseModel):
    name: str


class PortfolioBase(BaseModel):
    name: str
    price: str


class PortfolioResponse(BaseModel):
    id: int
    name: str
    price: str
    created_at: datetime