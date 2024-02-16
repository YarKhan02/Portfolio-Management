from fastapi import FastAPI

from .routers import portfolio, auth, user


port = FastAPI()

port.include_router(portfolio.router)
port.include_router(portfolio.user)
port.include_router(portfolio.auth)


@port.get("/")
def read_root():
    return {"My Name": "Wali yar khan"}