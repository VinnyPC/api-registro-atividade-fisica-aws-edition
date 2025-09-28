from flask import Flask
from app.routes.atividades_routes import atividades
from app.models.atividade_model import Atividade
from flask_sqlalchemy import SQLAlchemy
from app.extensions import db_atividades
import os
from loguru import logger
from dotenv import load_dotenv
import pymysql

load_dotenv()


DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT = int(os.getenv('DB_PORT', 3306))
DB_USER = os.getenv('DB_USER', 'root')
DB_PASS = os.getenv('DB_PASS', '')
DB_NAME = os.getenv('DB_NAME', 'db_atividades')


def create_app():
    try:
        app = Flask(__name__)

        logger.info("Configurando banco de dados...")
        app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db_atividades.init_app(app)

        logger.info("Registrando blueprints")
        app.register_blueprint(atividades)

        return app
    except Exception as e:
        logger.error(f"Erro ao configurar banco de dados: {e}")
        raise


if __name__ == "__main__":
    try:
        logger.info("Verificando se o banco de dados existe...")
        conn = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        logger.info(f"Banco de dados '{DB_NAME}' criado ou já existente.")
        conn.close()
    except Exception as e:
        logger.error(f"Erro ao criar banco de dados: {e}")
        raise

    app = create_app()
    with app.app_context():
        db_atividades.create_all()
        logger.info("Tabelas criadas com sucesso!")
