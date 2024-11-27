from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Machine
from app.schemas import MachineCreate, MachineResponse
from app.database import get_db

router = APIRouter(prefix="/machines", tags=["Máquinas"])

@router.post("/", response_model=MachineResponse)
def create_machine(machine: MachineCreate, db: Session = Depends(get_db)):
    db_machine = Machine(**machine.dict())
    db.add(db_machine)
    db.commit()
    db.refresh(db_machine)
    return db_machine

@router.get("/", response_model=list[MachineResponse])
def list_machines(db: Session = Depends(get_db)):
    return db.query(Machine).all()
