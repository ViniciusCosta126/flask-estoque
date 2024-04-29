from app.routes import Blueprint, jsonify
from app.models import Produto

produtos_routes = Blueprint("produtos", __name__)


@produtos_routes.route('/produtos', methods=['GET'])
def index():
    produtos = Produto.query.all()
    return jsonify(produtos)
