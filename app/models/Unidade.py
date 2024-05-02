from app.models import db
from app.models import SerializerMixin


class Unidade(db.Model, SerializerMixin):
    """Classe para representar a unidade de medida dos itens em estoque."""
    __tablename__ = 'unidades'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(3), nullable=False)
    produtos = db.relationship('Produto', backref='unidade', lazy=True)
