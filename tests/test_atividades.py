import json

def test_create_atividade(client):
    payload = {
        "funcional": "001",
        "nome": "Basquete",
        "descricao": "Treino de basquete",
        "tipo": "Esporte",
        "duracao": 60,
        "distancia": 0,
        "intensidade": "Alta",
        "data": "2025-01-15",
        "calorias": 500
    }

    response = client.post("/atividades/", json=payload)
    data = response.get_json()

    assert response.status_code == 201
    assert "id" in data
    assert data["message"] == "Atividade criada!"

def test_create_atividade_invalid(client):
    payload = {"nome": "Sem funcional"} 

    response = client.post("/atividades/", json=payload)
    data = response.get_json()

    assert response.status_code == 400
    assert "error" in data

def test_get_atividades(client):
    payload1 = {"funcional": "001", "nome": "Basquete", "descricao": "", "tipo": "Esporte", "duracao": 60, "distancia": 0, "intensidade": "Alta", "data": "2025-01-15", "calorias": 500}
    payload2 = {"funcional": "002", "nome": "Corrida", "descricao": "", "tipo": "Cardio", "duracao": 30, "distancia": 5, "intensidade": "Média", "data": "2025-01-16", "calorias": 300}
    client.post("/atividades/", json=payload1)
    client.post("/atividades/", json=payload2)

    response = client.get("/atividades/")
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) == 2

    response = client.get("/atividades/?tipo=Cardio")
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["tipo"] == "Cardio"

def test_get_atividades_by_funcional(client):
    payload = {"funcional": "003", "nome": "Yoga", "descricao": "", "tipo": "Alongamento", "duracao": 45, "distancia": 0, "intensidade": "Baixa", "data": "2025-01-17", "calorias": 150}
    client.post("/atividades/", json=payload)

    response = client.get("/atividades/003")
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["funcional"] == "003"
