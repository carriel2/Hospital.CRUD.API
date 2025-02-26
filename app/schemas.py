from datetime import date, datetime
from pydantic import BaseModel


class PacienteBase(BaseModel):
    nome: str
    data_nascimento: date
    genero: str


class PacienteCreate(PacienteBase):
    pass


class Paciente(PacienteBase):
    id: int

    class Config:
        from_attributes = True


class MedicoBase(BaseModel):
    nome: str
    especialidade: str


class MedicoCreate(MedicoBase):
    pass


class Medico(MedicoBase):
    id: int

    class Config:
        from_attributes = True


class AgendamentoBase(BaseModel):
    data: datetime
    paciente_id: int
    medico_id: int


class AgendamentoCreate(BaseModel):
    pass


class Agendamento(AgendamentoBase):
    id: int

    class Config:
        from_attributes = True


class TratamentoBase(BaseModel):
    descricao: str
    agendamento_id: int


class TratamentoCreate(TratamentoBase):
    pass


class Tratamento(TratamentoBase):
    id: int

    class Config:
        from_attributes = True
