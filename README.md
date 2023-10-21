# FastApi project
### Frontend docs: https://github.com/inpanica/dgtu2023-frontend
## .env (must be in root directory)
```
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
HOST=
PORT=""
SECRET_MANAGER=""
SECRET_JWT=""
```
## Launch for local development
```
python -m venv venv
```
```
.\venv\Scripts\activate
```
```
pip install -r .\requirements.txt
```
```
alembic revision --autogenerate
```
```
alembic upgrade head
```
```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
## Launch in docker
```
docker-compose up --build
```
## http://your_host:8000/docs - swagger ui
# Used technologies
### [FastApi](https://fastapi.tiangolo.com/)
### [FastApi Users](https://fastapi-users.github.io/fastapi-users/12.1/)
### [Sqlalchemy](https://www.sqlalchemy.org/)
### [Alembic](https://alembic.sqlalchemy.org/en/latest/)
### [Pydantic](https://docs.pydantic.dev/latest/)
### [PostgreSQL](https://www.postgresql.org/)

# API Documentation
## Publications service
### 1. http://your_host:8000/articles/all - returns all articles (get)
```
{
  "status": "success",
  "data": [
    {
      "title": "string",
      "description": "string",
      "theme": "string",
      "date": "10.10.2005",
      "user_name": "string",
      "id": 1,
      "file_name": "string"
    },
    {
      "title": "cool title",
      "description": "my_desc",
      "theme": "sky",
      "date": "10.11.2005",
      "user_name": "aleks",
      "id": 2,
      "file_name": "devops.jpg"
    }
  ],
  "details": null
}
```
### 2. http://your_host:8000/articles/add_article - add article (post) 
#### input
```
{
  "user_name": "string",
  "title": "string",
  "description": "string",
  "date": "string",
  "theme": "string",
  "file_name": "string" 
}
```
#### output
```
{
  "status": "success"
}
```
### 3. http://your_host:8000/articles/add_photo - add photo
#### input
```
file
```

#### output
```
{
  "status": "success"
}
```
### 4. http://your_host:8000/articles/get_photo - get photo
#### input
```
{
"article_id": 1
}
```

#### output 
```
devops.jpg
```

# Test API 
```
pytest -v -s tests/
```

