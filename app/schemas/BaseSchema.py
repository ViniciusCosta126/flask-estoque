from app.schemas import Schema


class BaseSchema(Schema):
    class Meta:
        error_messages = {
            "required": "Campo obrigatório.",
            "null": "Este campo não pode ser nulo.",
            "type": "Tipo incorreto.",
            "unknown": "Campo não reconhecido"
        }
