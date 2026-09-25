from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API Questão 4 - Modelos")

# Schema Pydantic pra gerar a interface do SWAGGER com os mesmos campos
class AlunoSchema(BaseModel):
    id: int
    nome: str
    cpf: str
    disciplina: str
    turma: str
    universidade: str
    cidade: str
    professora: str

# Rota POST apenas pro Swagger compilar o Schema visualmente
@app.post("/alunos/", response_model=AlunoSchema)
async def consultar_aluno(aluno: AlunoSchema):
    return aluno