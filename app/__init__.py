from flask import Flask
from app.routes.atividades_routes import atividades
from app.extensions import db_atividades
from dotenv import load_dotenv
import os
from loguru import logger
from app.exceptions.errors import register_error_handlers

load_dotenv()

def configure_logger():
    if not os.path.exists("logs"):
        os.mkdir("logs")

    logger.add(
        "logs/app.log",
        rotation="10 MB",
        retention="10 days",
        level="INFO",
        backtrace=True,
        diagnose=True
    )
    return logger

def create_app():
    try:
        app = Flask(__name__)
        logger = configure_logger()

        # sqllite
        db_url = os.getenv("DB_URL", "sqlite:///atividades.db")

        #myqsl
        if not os.getenv("DB_URL"):
            DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
            DB_PORT = int(os.getenv('DB_PORT', 3306))
            DB_USER = os.getenv('DB_USER', 'root')
            DB_PASS = os.getenv('DB_PASS', '')
            DB_NAME = os.getenv('DB_NAME', 'db_atividades')
            db_url = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

        app.config['SQLALCHEMY_DATABASE_URI'] = db_url
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db_atividades.init_app(app)

        app.register_blueprint(atividades)

        with app.app_context():
            from app.models import atividade_model
            db_atividades.create_all()
            logger.info("Tabelas criadas com sucesso!")

        register_error_handlers(app)
        logger.info("App inicializado com sucesso!")
        return app
    except Exception as e:
        logger.error(f"Erro ao configurar banco de dados: {e}")
        raise e
