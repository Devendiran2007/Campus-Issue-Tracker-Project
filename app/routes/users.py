from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/users",tags=["Users"])

@router.post("/",response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate,db: Session = Depends(get_db)):
    new_user = models.User(
        name = user.name,
        email = user.email,
        password= user.password,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()