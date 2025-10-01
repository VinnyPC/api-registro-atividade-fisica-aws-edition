#script criado para popular automaticamente o banco de dados em caso de teste

from app.extensions import db_atividades
from app.models.atividade_model import Atividade
from datetime import datetime
from app.repositories.atividade_repository import AtividadeRepository
from loguru import logger
from app import create_app

app = create_app()

def populate():
    try:
        logger.info("Populando banco de dados com dados de teste...")

        atividades_teste = [
            {
                "funcional": "1234567",
                "dataHora": "2000-09-30T07:30:00",
                "codigoAtividade": "RUN",
                "descricaoAtividade": "Correr 5km"
            },
            {
                "funcional": "1234568",
                "dataHora": "2001-01-15T18:45:00",
                "codigoAtividade": "BIKE",
                "descricaoAtividade": "Pedalar 20km"
            },
            {
                "funcional": "1234569",
                "dataHora": "2002-03-10T06:15:00",
                "codigoAtividade": "SWIM",
                "descricaoAtividade": "Nadar 1km"
            },
            {
                "funcional": "1234570",
                "dataHora": "2003-05-05T19:00:00",
                "codigoAtividade": "GYM",
                "descricaoAtividade": "Treino de musculação"
            },
            {
                "funcional": "1234571",
                "dataHora": "2004-07-21T07:10:00",
                "codigoAtividade": "RUN",
                "descricaoAtividade": "Corrida de 10km"
            },
            {
                "funcional": "1234572",
                "dataHora": "2005-09-12T12:30:00",
                "codigoAtividade": "HIKE",
                "descricaoAtividade": "Trilha de 5km"
            },
            {
                "funcional": "1234573",
                "dataHora": "2006-11-30T16:00:00",
                "codigoAtividade": "ROW",
                "descricaoAtividade": "Remar por 45 minutos"
            },
            {
                "funcional": "1234574",
                "dataHora": "2007-02-14T20:20:00",
                "codigoAtividade": "BOX",
                "descricaoAtividade": "Treino de boxe"
            },
            {
                "funcional": "1234575",
                "dataHora": "2008-04-28T08:40:00",
                "codigoAtividade": "RUN",
                "descricaoAtividade": "Corrida leve de 3km"
            },
            {
                "funcional": "1234576",
                "dataHora": "2009-08-09T17:25:00",
                "codigoAtividade": "YOGA",
                "descricaoAtividade": "Sessão de yoga 1h"
            }
        ]

        with app.app_context():
            for data in atividades_teste:
                data["dataHora"] = datetime.fromisoformat(data["dataHora"])
                AtividadeRepository.create(data)

        logger.success("Banco de dados populado com sucesso!")

    except Exception as e:
        logger.error(f"Erro ao popular banco de dados: {e}", exc_info=True)

if __name__ == "__main__":
    populate()