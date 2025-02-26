from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    data_nascimento = Column(Date)
    genero = Column(String)
    agendamentos = relationship(
        "Agendamento", back_populates="paciente", cascade="all, delete"
    )


class Medico(Base):
    __tablename__ = "medicos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    especialidade = Column(String)
    agendamentos = relationship(
        "Agendamento", back_populates="medico", cascade="all, delete"
    )


class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Integer, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    medico_id = Column(Integer, ForeignKey("medicos.id"))

    paciente = relationship("Paciente", back_populates="agendamentos")
    medico = relationship("Medico", back_populates="agendamentos")
    tratamentos = relationship(
        "Tratamento", back_populates="agendamentos", cascade="all, delete"
    )


class Tratamento(Base):
    __tablename__ = "tratamentos"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)
    agendamento_id = Column(Integer, ForeignKey("agendamentos.id"))

    agendamento = relationship("Agendamento", back_populates="tratamentos")
