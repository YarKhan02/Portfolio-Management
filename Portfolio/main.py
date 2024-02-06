from fastapi import FastAPI

from .routers import portfolio


port = FastAPI()

port.include_router(portfolio.router)


@port.get("/")
def read_root():
    return {"My Name": "Wali yar khan"}