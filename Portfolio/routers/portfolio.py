from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from typing import List, Optional

from sqlalchemy.orm import Session, aliased
from sqlalchemy import func

from .. import models, schemas, calculation, outh2
from ..database import get_db


router = APIRouter(prefix = '/portfolio', tags = ['Portfolio'])



@router.get('/', response_model = List[schemas.PortfolioBase])
def all_crypto_holdings(db: Session = Depends(get_db)):
    cryptocurrency = db.query(models.Portfolio).all()
    
    return cryptocurrency 



@router.post('/', response_model = schemas.PortfolioRespose)
def add_in_portfolio(entry: schemas.PortfolioAdded, db: Session = Depends(get_db), current_user: int = Depends(outh2.get_current_user)):
    calculation.portfolio_entry(entry)

    new_entry = models.Portfolio(owner_id = current_user.id, **add.dict()) # **to_add unpack all fields
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    
    return new_entry



@router.put('/acquire', response_model = schemas.PortfolioBase)
def update_acquire(add: schemas.TokenValidity, db: Session = Depends(get_db)):
    query = db.query(models.Portfolio).filter(models.Portfolio.name == add.name)
    crypto = query.first()

    if crypto == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'{add.name} does not exist')

    calculation.calculate_buy(crypto, add)

    # if crypto.owner_id != current_user.id:
    #     raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = 'Not authorized to perform requested action')

    query.update(add.dict(), synchronize_session = False)
    db.commit()

    return query.first()



@router.put('/remove', response_model = schemas.PortfolioBase)
def update_remove(rm: schemas.TokenValidity, db: Session = Depends(get_db)):
    query = db.query(models.Portfolio).filter(models.Portfolio.name == rm.name)
    sell = query.first()
    
    if sell == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'{rm.name} does not exist')

    try:
        calculation.calculate_sell(sell, rm)

    except HTTPException as e:
        return e

    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = 'Not authorized to perform requested action')

    query.update(rm.dict(), synchronize_session = False)
    db.commit()    
    


@router.delete('/', status_code = status.HTTP_204_NO_CONTENT)
def delete_entry(name: schemas.NameCheck, db: Session = Depends(get_db)):
    query = db.query(models.Portfolio).filter(models.Portfolio.name == name.name)
    to_delete = query.first()

    if to_delete == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'{name.name} does not exist')

    query.delete(synchronize_session = False)
    db.commit()

    return Response(status_code = status.HTTP_404_NOT_FOUND)