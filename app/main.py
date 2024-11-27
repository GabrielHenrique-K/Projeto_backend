from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from app.database import Base, engine
from app.routers import machines, maintenances, inventory, users
from app import auth

# Inicialize o banco de dados
Base.metadata.create_all(bind=engine)

# Inicialize o app FastAPI
app = FastAPI(
    title="Sistema de Gerenciamento de Manutenção",
    description="API para gerenciar máquinas, manutenções e estoque.",
    version="1.0.0",
    docs_url="/docs",  # URL para a documentação Swagger
    redoc_url="/redoc"  # URL para a documentação ReDoc
)

# Esquema de autenticação para Swagger
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# Inclua os routers
app.include_router(machines.router)
app.include_router(maintenances.router)
app.include_router(inventory.router)
app.include_router(users.router)
app.include_router(auth.router)
