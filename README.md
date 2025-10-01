# API de Registro de Atividades Físicas

API RESTful simples que permite o **registros** e **consultas** de atividades físicas realizadas por funcionários.

---

## Tecnologias

- Python 3.11+
- Flask
- SQLAlchemy
- SQLite
- Pytest (testes unitários)
- Loguru (logs)
- python-dotenv (variáveis de ambiente)
---
## Features

- **Criação e configuração do banco de dados** facilitada com `setup_db` em caso de uso com MySQL.
- **Configuração de ambiente** simplificada com `requirements.txt`.
- **Variáveis de ambiente** para segurança (conexão com banco, senhas e secrets).
- **Validação de dados** com **Marshmallow**, garantindo que apenas dados corretos sejam processados.
- **Respostas intuitivas ao cliente**: mensagens claras e apropriadas de acordo com o método HTTP e feedback em caso de erro.
- Gravação e consulta: operações de consulta e gravação totalmente implementadas (branch `versao-aprimorada-crud`).
- **Paginação e filtros**:
  - Filtrar por tipo de atividade: `/atividades?codigoAtividade=RUN`
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

Configurar variáveis de ambiente para no arquivo `.env` (MySQL):

```bash
  DB_USER=root
  DB_PASS=root
  DB_HOST=127.0.0.1
  DB_PORT=3306
  DB_NAME=db_atividades
```
Configurar variáveis de ambiente para no arquivo `.env` (SQLite):
```bash
  DB_URL=sqlite:///atividades.db
```

### (MySQL) Inicialização do Banco de Dados ao iniciar a API localmente pela primeira vez
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
| GET        | /atividades?codigoAtividade=<tipo>     | Filtrar atividades por codigo da atividade (ex: `/atividades?codigoAtividade=GYM`)   |
| GET        | /atividades?data_inicio=<YYYY-MM-DDTHH:MM:SS>&data_fim=<YYYY-MM-DDTHH:MM:SS> | Filtrar atividades por intervalo de datas |
| GET        | /atividades?page=<n>&per_page=<m> | Paginar resultados (ex: `/atividades?page=1&per_page=10`) |


---

### Testes feitos via insomnia 

#### Registrar uma nova atividade física
**Exemplo**: `POST http://127.0.0.1:5000/atividades/`
  
<img width="1127" height="572" alt="image" src="https://github.com/user-attachments/assets/a0deddf1-ccc6-452b-9aba-3c42457ecc6f" />


#### Listar todas as atividades registradas
**Exemplo**: `GET http://127.0.0.1:5000/atividades/`
  
<img width="1202" height="556" alt="image" src="https://github.com/user-attachments/assets/2d3f4c41-e9fb-46fe-8f0e-51e7b5382321" />

---
### Filtros: Você pode refinar sua busca usando um ou mais filtros na sua API via query string!


#### Listar todas as atividades de um funcionário específico
**Exemplo**: `GET http://127.0.0.1:5000/atividades/<funcional>`  
  
<img width="1107" height="619" alt="image" src="https://github.com/user-attachments/assets/090242e7-756a-4c87-9724-fff0edc067c3" />


#### Listar todas as atividades em um período específico
**Exemplo**: `GET http://127.0.0.1:5000/atividades?dataHora_inicio=<AAAA-MM-DDTHH:MM:SS>&dataHora_fim=<AAAA-MM-DDTHH:MM:SS>`
  
<img width="1130" height="648" alt="image" src="https://github.com/user-attachments/assets/7933ac7a-2a47-4ae3-8e96-df62bc0f84d4" />

#### Listar todas as atividades filtrando o código da atividade
**Exemplo**: `GET http://127.0.0.1:5000/atividades?codigoAtividade=GYM`  
  
<img width="1317" height="679" alt="image" src="https://github.com/user-attachments/assets/ddc1d1b4-fc0f-476e-96a2-aab4efe90130" />

#### Listar todas as atividades com código "GYM" e que estão cadastadas com datas entre 24/09/2025 às 07:00 e 30/09/2025 às 08:30:00, além disso, visualizar a primeira página e mostrar apenas 4 itens por página
**Exemplo**: `GET http://127.0.0.1:5000/atividades?dataHora_inicio=2025-09-24T07:00:00&dataHora_fim=2026-09-30T08:30:00&codigoAtividade=GYM&page=1&per_page=4`  

<img width="1251" height="822" alt="image" src="https://github.com/user-attachments/assets/f0dc2ba7-0b20-425f-8c9c-e9970a2e44be" />









