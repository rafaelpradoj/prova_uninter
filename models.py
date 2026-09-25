from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# aqui estou criando a classe base declarativa
Base = declarative_base()

# aqui estou definindo a classe mapeada com os campos solicitados
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