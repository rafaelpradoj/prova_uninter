from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Define o nome e o caminho do banco de dados local
SQLALCHEMY_DATABASE_URL = "sqlite:///./alunos.db"

# Cria o motor do banco. (check_same_thread=False é exigido pelo SQLite no FastAPI)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Configuração da sessão que será injetada nas rotas do main.py
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base que o models.py vai utilizar
Base = declarative_base()