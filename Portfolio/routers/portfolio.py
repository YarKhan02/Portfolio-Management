from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from typing import List, Optional

from sqlalchemy.orm import Session, aliased
from sqlalchemy import func

from .. import models, schemas, utils 
from ..database import get_db


router = APIRouter(prefix = '/portfolio', tags = ['Portfolio'])



@router.get('/', response_model = List[schemas.PortfolioBase])
def all_crypto_holdings(db: Session = Depends(get_db)):
    cryptocurrency = db.query(models.Portfolio).all()
    
    return cryptocurrency 



@router.post('/', response_model = schemas.PortfolioBase)
def add_in_portfolio(add: schemas.TokenValidity, db: Session = Depends(get_db)):
    to_add = get_token(add)

    addition = models.Portfolio(**to_add) # **to_add unpack all fields
    db.add(addition)
    db.commit()
    db.refresh(addition)
    
    return to_add 



@router.put('/', response_model = schemas.PortfolioBase)
def update(add: schemas.TokenValidity, db: Session = Depends(get_db)):
    query = db.query(models.Portfolio).filter(models.Portfolio.name == add.name)
    crypto = query.first()

    if crypto == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'{add.name} does not exist')

    new_entry = utils.get_token(add)
    to_update = utils.calculate(crypto, new_entry)

    # if crypto.owner_id != current_user.id:
    #     raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = 'Not authorized to perform requested action')

    db.commit()

    return query.first()



@router.delete('/', response_class = schemas.PortfolioBase)
def update(rm: schemas.TokenValidity, db: Session = Depends(get_db)):
    query = db.query(models.Portfolio).filter(models.Portfolio.name == rm.name)
    sell = query.first()
    
    if sell == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'{rm.name} does not exist')

    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = 'Not authorized to perform requested action')

    # query.delete(synchronize_session = False)
    db.commit()
    
    return Response(status_code = status.HTTP_404_NOT_FOUND)