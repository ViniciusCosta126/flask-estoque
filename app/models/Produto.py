from app.models import db
from datetime import datetime
from app.models import SerializerMixin


class Produto(db.Model, SerializerMixin):
    """Classe para representar produtos no estoque"""
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricacao = db.Column(db.String(255), nullable=True)
    update_at = db.Column(db.Date, default=datetime.utcnow,
                          onupdate=datetime.utcnow)
    quantidade = db.Column(db.Integer, default=0)
    unidade_id = db.Column(db.Integer, db.ForeignKey('unidades.id'))
