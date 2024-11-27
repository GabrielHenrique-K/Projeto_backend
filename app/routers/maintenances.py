from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Maintenance, Machine
from app.schemas import MaintenanceCreate, MaintenanceResponse
from app.database import get_db

router = APIRouter(prefix="/maintenances", tags=["Manutenções"])

@router.post("/", response_model=MaintenanceResponse)
def create_maintenance(maintenance: MaintenanceCreate, db: Session = Depends(get_db)):
    machine = db.query(Machine).filter(Machine.id == maintenance.machine_id).first()
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    db_maintenance = Maintenance(**maintenance.dict(), status="pending")
    db.add(db_maintenance)
    db.commit()
    db.refresh(db_maintenance)
    return db_maintenance

@router.get("/", response_model=list[MaintenanceResponse])
def list_maintenances(db: Session = Depends(get_db)):
    return db.query(Maintenance).all()
