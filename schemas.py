from pydantic import BaseModel

# Classe base
class AlunoBase(BaseModel):
    nome: str
    cpf: str
    disciplina: str
    turma: str
    universidade: str
    cidade: str
    professora: str

# Schema usado na hora de receber os dados (POST)
class AlunoCreate(AlunoBase):
    pass

# Schema usado na hora de devolver os dados, agora incluindo o ID gerado pelo banco
class AlunoResponse(AlunoBase):
    id: int

    class Config:
        from_attributes = True