from sqlalchemy import Column, Integer, String
from database import Base

class AlunoModel(Base):
    __tablename__ = 'alunos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cpf = Column(String)
    disciplina = Column(String)
    turma = Column(String)
    universidade = Column(String)
    cidade = Column(String)
    professora = Column(String)