from datetime import datetime, timedelta

import prisma
import prisma.models
from fastapi import HTTPException, status
from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseModel


class LoginOutput(BaseModel):
    """
    The response model for a successful login attempt, returning a session token for authenticated access.
    """

    token: str
    message: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "a_very_secret_key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def authenticate_user(username: str, password: str):
    user = await prisma.models.User.prisma().find_unique(where={"email": username})
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def login(username: str, password: str) -> LoginOutput:
    """
    Handles user login, issuing tokens for authenticated sessions.

    Args:
    username (str): The username of the user trying to log in.
    password (str): The password of the user trying to log in.

    Returns:
    LoginOutput: The response model for a successful login attempt, returning a session token for authenticated access.
    """
    user = await authenticate_user(username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return LoginOutput(token=access_token, message="Login successful")
