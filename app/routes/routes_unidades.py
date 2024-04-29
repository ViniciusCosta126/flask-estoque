from app.routes import jsonify, Blueprint, request
from app.models import Unidade
from app import db

unidades_routes = Blueprint('unidades', __name__)


@unidades_routes.route('/unidades', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        unidades = [u.to_dict() for u in Unidade.query.all()]
        return jsonify({'unidades': unidades}), 200
    else:
        unidade = Unidade(nome=request.json['nome'])
        db.session.add(unidade)
        db.session.commit()
        return jsonify(unidade.to_dict()), 201


@unidades_routes.route('/unidades/<int:id>', methods=['DELETE', 'PATCH', 'PUT'])
def delete_and_update_unidade(id):
    unidade = Unidade.query.get(id)
    if unidade is None:
        return jsonify({"message": 'Uninidade não encontrada!'}), 404
    else:
        if request.method == 'DELETE':
            try:
                db.session.delete(unidade)
                db.session.commit()
                return '', 204
            except Exception as e:
                db.session.rollback()
                return jsonify({"message": str(e)}), 500
        else:
            try:
                unidade.nome = request.json['nome']
                db.session.commit()
                return jsonify({"message": "Unidade atualizada com sucesso!", "unidade": unidade.to_dict()}), 200
            except Exception as e:
                db.session.rollback()
                return jsonify({"message": str(e)}), 500
