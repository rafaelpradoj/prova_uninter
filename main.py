from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, SessionLocal

# Esta linha cria fisicamente a tabela 'alunos' no arquivo SQLite
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Questão 4 - Modelos")
@app.get("/")
def raiz():
    return {"message": "API da Questão 4 rodando perfeitamente. Acesse /docs para o Swagger."}

# Injeção de dependência exigida para operar o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota POST real operando o SQLAlchemy
@app.post("/alunos/", response_model=schemas.AlunoResponse)
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    # Converte os dados validados do Pydantic para o modelo do SQLAlchemy
    db_aluno = models.AlunoModel(**aluno.model_dump())
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno