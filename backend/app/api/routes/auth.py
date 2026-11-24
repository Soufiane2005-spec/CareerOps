
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_user_by_email
from app.schemas.user import UserCreate, UserResponse, UserLogin
router = APIRouter(prefix="/auth", tags=["Authentication"])
from app.services.user_service import (
    create_user,
    get_user_by_email,
    authenticate_user,
)

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user_data: UserCreate,
    db: Annotated[Session, Depends(get_db)],
):
    existing_user = get_user_by_email(db, user_data.email)

    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    try:
        user = create_user(
            db=db,
            email=user_data.email,
            password=user_data.password,
        )
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        ) from None

    return user

@router.post(
    "/login",
    response_model=UserResponse,
    responses={
        401: {"description": "Invalid email or password"}
    },
)
def login(
    user_data: UserLogin,
    db: Annotated[Session, Depends(get_db)],
):
    user = authenticate_user(
        db=db,
        email=user_data.email,
        password=user_data.password,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    return user
