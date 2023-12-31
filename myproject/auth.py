

import os #voor github secrets

# pip install python-multipart      (deze stond niet in de cursus)
# pip install "passlib[bcrypt,argon2]"
from passlib.context import CryptContext
import crud

from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

from jose import JWTError, jwt
from datetime import datetime, timedelta

#SECRET_KEY = os.environ.get("SECRET_KEY")
#ALGORITHM = os.environ.get("ALGORITHM")
#ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
print("ALGORITHM:", ALGORITHM)

#OAuth
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#HASHING
def get_password_hash(password):
    return pwd_context.hash(password)

#0Auth
pwd_context = CryptContext(schemes=["bcrypt", "argon2"], deprecated="auto")
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str):
    user = crud.get_author_by_email(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

#token
def create_access_token(data: dict):
    to_encode = data.copy()
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        # Default to 15 minutes of expiration time if ACCESS_TOKEN_EXPIRE_MINUTES variable is empty
        expire = datetime.utcnow() + timedelta(minutes=15)
    # Adding the JWT expiration time case
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_author(db: Session, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = crud.get_author_by_email(db, username)
    if user is None:
        raise credentials_exception
    return user
    
def get_current_active_user(db: Session, token: str = Depends(oauth2_scheme)):
    current_user = get_current_author(db, token)
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
