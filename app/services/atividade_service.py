from app.repositories.atividade_repository import AtividadeRepository
from loguru import logger

class AtividadeService:
    @staticmethod
    def criar_atividade(data: dict):
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
