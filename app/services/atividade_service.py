from app.repositories.atividade_repository import AtividadeRepository
from loguru import logger

class AtividadeService:
    REQUIRED_FIELDS = [
        "funcional", "nome", "descricao", "tipo",
        "duracao", "distancia", "intensidade", "data", "calorias"
    ]
    @staticmethod
    def criar_atividade(data: dict):
        logger.info(f"Atividade criada: {id}")
        return AtividadeRepository.create(data)
    
    @staticmethod
    def listar_atividades(page=1, per_page=10, filters=None):
        return AtividadeRepository.get_paginated_and_filtered(page, per_page, filters)
    
    @staticmethod
    def buscar_todas():
        return AtividadeRepository.get_all()

    @staticmethod
    def buscar_por_funcional(funcional):
        return AtividadeRepository.get_by_funcional(funcional)
    
    @staticmethod
    def editar_atividade(id, data):
        atividade = AtividadeRepository.get_by_id(id)
        if not atividade:
            return None

        for key, value in data.items():
            if hasattr(atividade, key):
                setattr(atividade, key, value)

        return AtividadeRepository.update(atividade)

    @staticmethod
    def deletar_atividade(id):
        atividade = AtividadeRepository.get_by_id(id)
        if not atividade:
            return False
        AtividadeRepository.delete(atividade)
        return True