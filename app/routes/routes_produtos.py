from app import db
from app.routes import Blueprint, jsonify, request
from app.models import Produto
from app.schemas import ProdutoSchema, ValidationError

produtos_routes = Blueprint("produtos", __name__)


@produtos_routes.route('/produtos', methods=['GET'])
def get_produtos():
    try:
        produtos = [p.to_dict() for p in Produto.query.all()]
        return jsonify({'produtos': produtos}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@produtos_routes.route('/produto', methods=['POST'])
def create_produto():
    json_data = request.get_json()
    schema = ProdutoSchema()

    if not json_data:
        return jsonify({"message": "Dados Invalidos"}), 400

    try:
        data = schema.load(json_data)
    except ValidationError as err:
        return jsonify({"erros": err.messages}), 422

    produto = Produto(nome=json_data['nome'],
                      descricacao=json_data['descricacao'], quantidade=json_data['quantidade'], unidade_id=json_data['unidade_id'])
    db.session.add(produto)
    db.session.commit()
    return jsonify(produto.to_dict()), 201
