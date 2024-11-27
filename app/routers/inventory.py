from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.models import Part
from app.schemas import PartCreate, PartResponse
from app.database import get_db

router = APIRouter(prefix="/inventory", tags=["Estoque"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

@router.post("/parts", response_model=PartResponse)
def create_part(part: PartCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_part = Part(**part.dict())
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part

@router.get("/parts", response_model=list[PartResponse])
def list_parts(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return db.query(Part).all()
