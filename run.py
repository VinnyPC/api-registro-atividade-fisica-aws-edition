from app import create_app, db_atividades
from app.models.atividade_model import Atividade
from loguru import logger

app = create_app()

with app.app_context(): 
    db_atividades.create_all()
    logger.success("Tabelas atualizadas com sucesso!")


if __name__ == "__main__":
    app.run(debug=True)

    
