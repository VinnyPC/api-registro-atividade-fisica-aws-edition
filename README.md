# API de Registro de Atividades Físicas

API RESTful simples que permite o **registros** e **consultas** de atividades físicas realizadas por funcionários.

---

## Tecnologias

- Python 3.11+
- Flask
- SQLAlchemy
- MySQL
- Pytest (testes unitários)
- Loguru (logs)
- python-dotenv (variáveis de ambiente)
---
## Features

- **Criação e configuração do banco de dados** facilitada com `setup_db`.
- **Configuração de ambiente** simplificada com `requirements.txt`.
- **Variáveis de ambiente** para segurança (conexão com banco, senhas e secrets).
- **Validação de dados** com **Marshmallow**, garantindo que apenas dados corretos sejam processados.
- **Respostas intuitivas ao cliente**: mensagens claras e apropriadas de acordo com o método HTTP e feedback em caso de erro.
- Gravação e consulta: operações de consulta e gravação totalmente implementadas (detalhes na outra branch).
- **Paginação e filtros**:
  - Filtrar por tipo: `/atividades?tipo=Basquete`
  - Filtrar por intervalo de datas: `/atividades?data_inicio=2025-01-01&data_fim=2025-01-31`
  - Paginar resultados: `/atividades?page=1&per_page=10`

---

## Código

- **Responsabilidades separadas** por arquivos `.py` (`routes`, `service`, `repository`, `models`, `schemas`), facilitando **manutenção, legibilidade e organização** do código.
- **Uso de testes unitários** para garantir a funcionalidade do código e reduzir regressões.
- **Uso de schemas com Marshmallow** para validação e serialização de dados, garantindo consistência entre API e banco de dados.
- **Logging centralizado** com Loguru, permitindo monitoramento de operações e erros de forma detalhada.
- **Tratamento de erros centralizado**, garantindo respostas consistentes para exceções e validações.


---
## Estrutura do projeto
```bash

📦 
├─ .gitignore
├─ README.md
├─ app
│  ├─ __init__.py
│  ├─ exceptions
│  │  └─ errors.py
│  ├─ extensions.py
│  ├─ models
│  │  └─ atividade_model.py
│  ├─ repositories
│  │  └─ atividade_repository.py
│  ├─ routes
│  │  └─ atividades_routes.py
│  ├─ schemas
│  │  └─ atividade_schema.py
│  └─ services
│     └─ atividade_service.py
├─ requirements.txt
├─ run.py
├─ setup_db.py
└─ tests
   ├─ __init__.py
   ├─ conftest.py
   └─ test_atividades.py
```
---

## Rodar localmente

Clone o projeto:
```bash
  git clone https://github.com/VinnyPC/api-registro-atividade-fisica.git
```

Vá para o diretório do projeto:

```bash
  cd api-registro-atividade-fisica
```

Criar e ativar o ambiente virtual:

```bash
  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate     # Windows
```

Instalar as dependências:

```bash
  pip install -r requirements.txt
```

Configurar variáveis de ambiente no arquivo (.env):

```bash
  DB_HOST=127.0.0.1
  DB_PORT=3306
  DB_USER=root
  DB_PASS=root
  DB_NAME=db_atividades
```

### Inicialização do Banco de Dados
Execute o script de setup para criar o banco e tabelas:

```bash
  python setup_db.py
```

### Rodando a API Localmente
Execute o script de setup para criar o banco e tabelas:

```bash
  python run.py
```
Por padrão, a API fica disponível em: http://127.0.0.1:5000

### Populando seu banco de dados
Execute o script para popular o banco de dados com vários registros:

```bash
  python populate_db.py
```


---
### Endpoints

| **Método** | **URL**                     | **Descrição**                                                    |
|------------|-----------------------------|------------------------------------------------------------------|
| POST       | /atividades/                | Criar nova atividade                                             |
| GET        | /atividades/                | Listar todas as atividades                                       |
| GET        | /atividades/<funcional>     | Buscar atividades pela funcional                                 |
| GET        | /atividades?tipo=<tipo>     | Filtrar atividades por tipo (ex: `/atividades?tipo=Basquete`)   |
| GET        | /atividades?data_inicio=<YYYY-MM-DD>&data_fim=<YYYY-MM-DD> | Filtrar atividades por intervalo de datas |
| GET        | /atividades?page=<n>&per_page=<m> | Paginar resultados (ex: `/atividades?page=1&per_page=10`) |


---

### Testes feitos via insomnia 

#### Registrar uma nova atividade física
<img width="1906" height="1029" alt="image" src="https://github.com/user-attachments/assets/de813ad4-c46b-49d6-b27c-700463af6001" />


#### Listar todas as atividades registradas
<img width="1915" height="1032" alt="image" src="https://github.com/user-attachments/assets/e0f04576-2a82-4ca5-b527-03de88de2ef3" />



#### Listar todas as atividades de um funcionário específico

<img width="1913" height="1036" alt="image" src="https://github.com/user-attachments/assets/d83519cc-fb32-47f6-a0bf-b768e50e6d19" />



