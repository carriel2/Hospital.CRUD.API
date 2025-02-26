from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas


async def get_paciente(db: AsyncSession, paciente_id: int):
    result = await db.execute(
        select(models.Paciente).where(models.Paciente.id == paciente_id)
    )
    return result.scalars().first()


async def get_pacientes(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(models.Paciente).offset(skip).limit(limit))
    return result.scalars().all()


async def create_paciente(db: AsyncSession, paciente: schemas.PacienteCreate):
    db_paciente = models.Paciente(**paciente.dict())
    db.add(db_paciente)
    await db.commit()
    await db.refresh(db_paciente)
    return db_paciente


async def update_paciente(
    db: AsyncSession, paciente_id: int, paciente_data: schemas.PacienteCreate
):
    db_paciente = await get_paciente(db, paciente_id)
    if db_paciente:
        for key, value in paciente_data.dict().items():
            setattr(db_paciente, key, value)
        await db.commit()
        await db.refresh(db_paciente)
    return db_paciente


async def delete_paciente(db: AsyncSession, paciente_id: int):
    db_paciente = await get_paciente(db, paciente_id)
    if db_paciente:
        await db.delete(db_paciente)
        await db.commit()
    return db_paciente


async def get_medico(db: AsyncSession, medico_id: int):
    result = await db.execute(
        select(models.Medico).where(models.Medico.id == medico_id)
    )
    return result.scalars().first()


async def get_medicos(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Medico).offset(skip).limit(limit))
    return result.scalars().all()


async def create_medico(db: AsyncSession, medico: schemas.MedicoCreate):
    db_medico = models.Medico(**medico.dict())
    db.add(db_medico)
    await db.commit()
    await db.refresh(db_medico)
    return db_medico


async def update_medico(
    db: AsyncSession, medico_id: int, medico_data: schemas.MedicoCreate
):
    db_medico = await get_medico(db, medico_id)
    if db_medico:
        for key, value in medico_data.dict().items():
            setattr(db_medico, key, value)
        await db.commit()
        await db.refresh(db_medico)
    return db_medico


async def delete_medico(db: AsyncSession, medico_id: int):
    db_medico = await get_medico(db, medico_id)
    if db_medico:
        await db.delete(db_medico)
        await db.commit()
    return db_medico


async def get_agendamento(db: AsyncSession, agendamento_id: int):
    result = await db.execute(
        select(models.Agendamento).where(models.Agendamento.id == agendamento_id)
    )
    return result.scalars().first()


async def get_agendamentos(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Agendamento).offset(skip).limit(limit))
    return result.scalars().all()


async def create_agendamento(db: AsyncSession, agendamento: schemas.AgendamentoCreate):
    db_agendamento = models.Agendamento(**agendamento.dict())
    db.add(db_agendamento)
    await db.commit()
    await db.refresh(db_agendamento)
    return db_agendamento


async def update_agendamento(
    db: AsyncSession, agendamento_id: int, agendamento_data: schemas.AgendamentoCreate
):
    db_agendamento = await get_agendamento(db, agendamento_id)
    if db_agendamento:
        for key, value in agendamento_data.dict().items():
            setattr(db_agendamento, key, value)
        await db.commit()
        await db.refresh(db_agendamento)
    return db_agendamento


async def delete_agendamento(db: AsyncSession, agendamento_id: int):
    db_agendamento = await get_agendamento(db, agendamento_id)
    if db_agendamento:
        await db.delete(db_agendamento)
        await db.commit()
    return db_agendamento


async def get_tratamento(db: AsyncSession, tratamento_id: int):
    result = await db.execute(
        select(models.Tratamento).where(models.Tratamento.id == tratamento_id)
    )
    return result.scalars().first()


async def get_tratamentos(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Tratamento).offset(skip).limit(limit))
    return result.scalars().all()


async def create_tratamento(db: AsyncSession, tratamento: schemas.TratamentoCreate):
    db_tratamento = models.Tratamento(**tratamento.dict())
    db.add(db_tratamento)
    await db.commit()
    await db.refresh(db_tratamento)
    return db_tratamento


async def update_tratamento(
    db: AsyncSession, tratamento_id: int, tratamento_data: schemas.TratamentoCreate
):
    db_tratamento = await get_tratamento(db, tratamento_id)
    if db_tratamento:
        for key, value in tratamento_data.dict().items():
            setattr(db_tratamento, key, value)
        await db.commit()
        await db.refresh(db_tratamento)
    return db_tratamento


async def delete_tratamento(db: AsyncSession, tratamento_id: int):
    db_tratamento = await get_tratamento(db, tratamento_id)
    if db_tratamento:
        await db.delete(db_tratamento)
        await db.commit()
    return db_tratamento
