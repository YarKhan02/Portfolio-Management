from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from typing import List, Optional

from sqlalchemy.orm import Session, aliased
from sqlalchemy import func

import requests

from . import models, schemas
from .database import get_db

port = FastAPI()


@port.get("/")
def read_root():
    return {"My Name": "Wali yar khan"}



def get_token(name):# db: Session = Depends(get_db), response_model = List[schemas.PortfolioResponse] 
    api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={name}&vs_currencies=usd"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for errors

        data = response.json()

    except requests.exceptions.RequestException as e:
        raise e

    result_dict = {'name': next(iter(data)), 'price': data[next(iter(data))]['usd']}

    return result_dict



@port.get('/portfolio', response_model = List[schemas.PortfolioBase])
def all_cryptocurrency(db: Session = Depends(get_db)):
    cryptocurrency = db.query(models.Portfolio).all()
    
    return cryptocurrency 



@port.post('/add')
def add_in_portfolio(add: schemas.TokenValidity, db: Session = Depends(get_db)):
    to_add = get_token(add.name)

    print(to_add)

    addition = models.Portfolio(**to_add) # **to_add unpack all fields
    db.add(addition)
    db.commit()
    db.refresh(addition)
    
    return to_add 