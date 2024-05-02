from app.schemas import BaseSchema, fields


class UnidadeSchema(BaseSchema):
    nome = fields.Str(required=True,)
