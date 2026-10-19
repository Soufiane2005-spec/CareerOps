
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.database import get_db


router = APIRouter()


@router.get("/db-check")
def check_database(
    db: Annotated[Session, Depends(get_db)],
):
    db.execute(text("SELECT 1"))

    return {"database": "connected"}
