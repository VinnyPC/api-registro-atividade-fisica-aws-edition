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
                "funcional": "12345",
                "nome": "Basquete",
                "descricao": "Treino de basquete",
                "tipo": "Esporte",
                "duracao": 60,
                "distancia": 0,
                "intensidade": "Alta",
                "data": datetime.strptime("2025-01-15", "%Y-%m-%d"),
                "calorias": 500
            },
            {
                "funcional": "12345",
                "nome": "Corrida",
                "descricao": "Corrida leve no parque",
                "tipo": "Cardio",
                "duracao": 30,
                "distancia": 5.0,
                "intensidade": "Média",
                "data": datetime.strptime("2025-01-16", "%Y-%m-%d"),
                "calorias": 300
            },
            {
                "funcional": "12345",
                "nome": "Yoga",
                "descricao": "Sessão de Yoga matinal",
                "tipo": "Alongamento",
                "duracao": 45,
                "distancia": 0,
                "intensidade": "Baixa",
                "data": "2025-01-17",
                "calorias": 150
            },
            {"funcional": "001", "nome": "Basquete", "descricao": "Treino de basquete", "tipo": "Esporte", "duracao": 60, "distancia": 0, "intensidade": "Alta", "data": "2025-01-19", "calorias": 500},
            {"funcional": "002", "nome": "Corrida", "descricao": "Corrida leve no parque", "tipo": "Cardio", "duracao": 30, "distancia": 5.0, "intensidade": "Média", "data": "2025-01-20", "calorias": 300},
            {"funcional": "003", "nome": "Yoga", "descricao": "Sessão de Yoga matinal", "tipo": "Alongamento", "duracao": 45, "distancia": 0, "intensidade": "Baixa", "data": "2025-01-21", "calorias": 150},
            {"funcional": "004", "nome": "Natação", "descricao": "Treino de natação", "tipo": "Esporte", "duracao": 50, "distancia": 1.2, "intensidade": "Alta", "data": "2025-01-22", "calorias": 400},
            {"funcional": "005", "nome": "Caminhada", "descricao": "Caminhada no parque", "tipo": "Cardio", "duracao": 40, "distancia": 3.5, "intensidade": "Média", "data": "2025-01-23", "calorias": 250},
            {"funcional": "006", "nome": "Pilates", "descricao": "Treino de Pilates", "tipo": "Alongamento", "duracao": 55, "distancia": 0, "intensidade": "Baixa", "data": "2025-01-24", "calorias": 200},
            {"funcional": "007", "nome": "Futebol", "descricao": "Treino de futebol", "tipo": "Esporte", "duracao": 70, "distancia": 2.5, "intensidade": "Alta", "data": "2025-01-25", "calorias": 600},
            {"funcional": "008", "nome": "Spinning", "descricao": "Aula de spinning", "tipo": "Cardio", "duracao": 45, "distancia": 0, "intensidade": "Alta", "data": "2025-01-26", "calorias": 450},
            {"funcional": "009", "nome": "Treino funcional", "descricao": "Treino com pesos e resistência", "tipo": "Musculação", "duracao": 60, "distancia": 0, "intensidade": "Alta", "data": "2025-01-27", "calorias": 500},
            {"funcional": "010", "nome": "Meditação", "descricao": "Sessão de meditação", "tipo": "Relaxamento", "duracao": 30, "distancia": 0, "intensidade": "Baixa", "data": "2025-01-28", "calorias": 50},
        ]

        with app.app_context():
            for data in atividades_teste:
                AtividadeRepository.create(data)

        logger.success("Banco de dados populado com sucesso!")

    except Exception as e:
        logger.error(f"Erro ao popular banco de dados: {e}", exc_info=True)

if __name__ == "__main__":
    populate()
