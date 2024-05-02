from app.schemas import BaseSchema, fields


class ProdutoSchema(BaseSchema):
    nome = fields.Str(required=True)
    descricacao = fields.Str(required=True)
    quantidade = fields.Int(required=True)
    unidade_id = fields.Int(required=True)
