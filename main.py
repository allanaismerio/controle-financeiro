from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
from models import Transacao

# Criar tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Static e Templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    transacoes = db.query(Transacao).order_by(Transacao.data.desc()).all()

    saldo = sum(
        t.valor if t.tipo == "receita" else -t.valor
        for t in transacoes
    )

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "transacoes": transacoes, "saldo": saldo}
    )

@app.post("/adicionar")
def adicionar(
    tipo: str = Form(...),
    descricao: str = Form(...),
    valor: float = Form(...),
    db: Session = Depends(get_db)
):
    nova = Transacao(tipo=tipo, descricao=descricao, valor=valor)
    db.add(nova)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/excluir/{id}")
def excluir(id: int, db: Session = Depends(get_db)):
    transacao = db.query(Transacao).filter(Transacao.id == id).first()
    if transacao:
        db.delete(transacao)
        db.commit()
    return RedirectResponse(url="/", status_code=303)
