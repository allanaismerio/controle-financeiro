from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Caminho do banco de dados SQLite
DATABASE_URL = "sqlite:///./financeiro.db"

# Criação do mecanismo de conexão
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Criação da sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os modelos
Base = declarative_base()
