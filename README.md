# FastAPI Book Manager

Um sistema completo de **gerenciamento de livros** construído com [FastAPI](https://fastapi.tiangolo.com/).  
Este projeto inclui **CRUD de livros**, **autenticação JWT**, **controle de permissões por usuário** e suporte a **PostgreSQL com SQLAlchemy + Alembic**.

---

## Features

- [x] Cadastro e autenticação de usuários (JWT)  
- [x] Diferentes papéis de usuário (`admin` / `user`)  
- [x] CRUD completo de livros  
- [x] Relacionamento `User ↔ Books` (favoritos)  
- [x] Filtros de busca por **autor, ano e rating**  
- [x] Validações com **Pydantic v2**  
- [x] Migrações de banco de dados com **Alembic**  
- [x] Testes automatizados com **Pytest**  
- [ ] Deploy em produção com Docker + Render/Heroku  

## Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Pytest](https://docs.pytest.org/)

## Estrutura de Pastas

```bash
fastapi-book-manager/
├── app/
│   ├── main.py           
│   ├── database.py       
│   ├── models.py        
│   ├── schemas.py  
│   ├── crud.py    
│   ├── routers/
│   │   ├── auth.py 
│   │   ├── users.py 
│   │   └── books.py 
│   ├── utils/
│   │   └── security.py 
├── tests/
│   ├── test_auth.py
│   ├── test_books.py
│   └── test_users.py
├── alembic/  
├── requirements.txt
└── README.md
