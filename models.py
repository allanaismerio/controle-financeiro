from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)  # 'receita' ou 'despesa'
    descricao = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(DateTime, default=datetime.utcnow)
