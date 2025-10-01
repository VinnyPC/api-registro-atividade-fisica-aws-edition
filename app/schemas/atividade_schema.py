from marshmallow import Schema, fields, validate

class AtividadeSchema(Schema):
    id = fields.Int(dump_only=True)
    funcional = fields.Str(required=True, validate=validate.Length(max=50))
    dataHora = fields.DateTime(required=True) 
    codigoAtividade = fields.Str(required=True, validate=validate.Length(max=50))
    descricaoAtividade = fields.Str(allow_none=True)
