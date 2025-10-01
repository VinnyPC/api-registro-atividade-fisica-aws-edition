from app.extensions import db_atividades

class Atividade(db_atividades.Model):
    __tablename__ = 'tb_atividades'

    id = db_atividades.Column(db_atividades.Integer, primary_key=True)
    funcional = db_atividades.Column(db_atividades.String(50), nullable=False)
    dataHora = db_atividades.Column(db_atividades.DateTime, nullable=False)
    codigoAtividade = db_atividades.Column(db_atividades.String(50), nullable=False)
    descricaoAtividade = db_atividades.Column(db_atividades.Text, nullable=True)

    def __repr__(self):
        return f"<Atividade id={self.id} funcional={self.funcional} codigoAtividade={self.codigoAtividade} dataHora={self.dataHora}>"

    def to_dict(self):
        return {
            "id": self.id,
            "funcional": self.funcional,
            "dataHora": self.dataHora.isoformat() if self.dataHora else None,
            "codigoAtividade": self.codigoAtividade,
            "descricaoAtividade": self.descricaoAtividade
        }