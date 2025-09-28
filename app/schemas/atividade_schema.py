from marshmallow import Schema, fields, validate

class AtividadeSchema(Schema):
    id = fields.Int(dump_only=True)
    funcional = fields.Str(required=True, validate=validate.Length(max=50))
    nome = fields.Str(required=True, validate=validate.Length(max=100))
    descricao = fields.Str(allow_none=True)
    tipo = fields.Str(allow_none=True)
    duracao = fields.Int(allow_none=True)
    distancia = fields.Float(allow_none=True)
    intensidade = fields.Str(allow_none=True)
    data = fields.Date(allow_none=True)
    calorias = fields.Int(allow_none=True)
