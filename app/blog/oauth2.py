from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from blog import token
from sqlalchemy.orm import Session
from . import database

get_db = database.get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(data: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return token.verify_token(data, credentials_exception, db)
