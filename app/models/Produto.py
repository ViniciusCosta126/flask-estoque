from app.models import db
from datetime import datetime


class Produto(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricacao = db.Column(db.String(255), nullable=True)
    update_at = db.Column(db.Date, default=datetime.utcnow,
                          onupdate=datetime.utcnow)
    quantidade = db.Column(db.Integer, default=0)
