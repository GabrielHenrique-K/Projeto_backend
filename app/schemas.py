from pydantic import BaseModel
from datetime import datetime

# Máquinas
class MachineCreate(BaseModel):
    name: str
    type: str
    model: str
    serial_number: str
    location: str
    manufacture_date: datetime

class MachineResponse(MachineCreate):
    id: int
    class Config:
        orm_mode = True

# Manutenções
class MaintenanceCreate(BaseModel):
    description: str
    priority: str
    machine_id: int

class MaintenanceResponse(MaintenanceCreate):
    id: int
    status: str
    requested_date: datetime
    class Config:
        orm_mode = True

# Estoque
class PartCreate(BaseModel):
    name: str
    code: str
    quantity: int

class PartResponse(PartCreate):
    id: int
    class Config:
        orm_mode = True

# Usuários
class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "user"

class UserResponse(BaseModel):
    id: int
    username: str
    role: str
    class Config:
        orm_mode = True

# Autenticação
class Token(BaseModel):
    access_token: str
    token_type: str
