import pytest
from app import create_app, db_atividades

@pytest.fixture
def app():
    app = create_app()

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True

    with app.app_context():
        db_atividades.create_all()
        yield app
        db_atividades.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
