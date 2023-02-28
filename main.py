from datetime import datetime, timedelta
from fastapi import Depends, FastAPI
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from api import auth
from api.routers import users, products
from db import models

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)
app.include_router(auth.router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "online"}
