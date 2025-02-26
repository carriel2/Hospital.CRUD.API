from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas, crud
from app.database import AsyncSessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Sistema Hospitalar API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/pacientes/", response_model=list[schemas.Paciente])
async def read_pacientes(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    pacientes = await crud.get_pacientes(db, skip=skip, limit=limit)
    return pacientes


@app.get("/pacientes/{paciente_id}", response_model=schemas.Paciente)
async def read_paciente(paciente_id: int, db: AsyncSession = Depends(get_db)):
    paciente = await crud.get_paciente(db, paciente_id=paciente_id)
    if paciente is not None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return paciente


@app.post("/pacientes/", response_model=schemas.Paciente)
async def create_paciente(
    paciente: schemas.PacienteCreate, db: AsyncSession = Depends(get_db)
):
    return await crud.create_paciente(db, paciente)


@app.put("/pacientes/{paciente_id}", response_model=schemas.Paciente)
async def update_paciente(
    paciente_id: int,
    paciente: schemas.PacienteCreate,
    db: AsyncSession = Depends(get_db),
):
    db_paciente = await crud.update_paciente(db, paciente_id, paciente)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return db_paciente


@app.delete("/pacientes/{paciente_id}")
async def delete_paciente(paciente_id: int, db: AsyncSession = Depends(get_db)):
    db_paciente = await crud.delete_paciente(db, paciente_id)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return {"detail": "Paciente deletado com suscesso"}


@app.get("/medicos/", response_model=list[schemas.Medico])
async def read_medicos(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    medicos = await crud.get_medicos(db, skip=skip, limit=limit)
    return medicos


@app.get("/medicos/{medico_id}", response_model=schemas.Medico)
async def read_medico(medico_id: int, db: AsyncSession = Depends(get_db)):
    medico = await crud.get_medico(db, medico_id=medico_id)
    if not medico:
        raise HTTPException(status_code=404, detail="Médico não encontrado")
    return medico


@app.post("/medico/", response_model=schemas.Medico)
async def create_medico(
    medico: schemas.MedicoCreate, db: AsyncSession = Depends(get_db)
):
    return await crud.create_medico(db, medico)


@app.put("/medicos/{medicos_id}", response_model=schemas.Medico)
async def update_medico(
    medico_id: int, medico: schemas.MedicoCreate, db: AsyncSession = Depends(get_db)
):
    db_medico = await crud.update_medico(db, medico_id, medico)
    if not db_medico:
        raise HTTPException(status_code=404, detail="Médico não encontrado")
    return db_medico


@app.delete("/medicos/{medico_id}")
async def delete_medico(medico_id: int, db: AsyncSession = Depends(get_db)):
    db_medico = await crud.delete_medico(db, medico_id)
    if not db_medico:
        raise HTTPException(status_code=404, detail="Médico não encontrado")
    return {"detail": "Médico deletado com sucesso"}


@app.get("/agendamento", response_model=list[schemas.Agendamento])
async def read_agendamentos(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    agendamentos = await crud.get_
