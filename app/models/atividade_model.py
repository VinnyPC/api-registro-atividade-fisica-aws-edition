from app.extensions import db_atividades

class Atividade(db_atividades.Model):
    __tablename__ = 'tb_atividades'

    id = db_atividades.Column(db_atividades.Integer, primary_key=True)
    funcional = db_atividades.Column(db_atividades.String(50), nullable=False)
    nome = db_atividades.Column(db_atividades.String(100), nullable=False)
    descricao = db_atividades.Column(db_atividades.Text)
    tipo = db_atividades.Column(db_atividades.String(50))
    duracao = db_atividades.Column(db_atividades.Integer)
    distancia = db_atividades.Column(db_atividades.Float)
    intensidade = db_atividades.Column(db_atividades.String(20))
    data = db_atividades.Column(db_atividades.Date)
    calorias = db_atividades.Column(db_atividades.Integer)

    def __repr__(self):
        return (
            f"<Atividade id={self.id} nome={self.nome} funcional={self.funcional} "
            f"tipo={self.tipo} data={self.data}>"
        )
    
    def to_dict(self):
        return {
            "id": self.id,
            "funcional": self.funcional,
            "nome": self.nome,
            "descricao": self.descricao,
            "tipo": self.tipo,
            "duracao": self.duracao,
            "distancia": self.distancia,
            "intensidade": self.intensidade,
            "data": self.data.strftime("%d/%m/%Y") if self.data else None,
            "calorias": self.calorias
        }