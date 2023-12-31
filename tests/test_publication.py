import pytest
from sqlalchemy import insert, select

from app.publication.models import Article
from conftest import client, async_session_maker


def test_article_add():
    response = client.post("/articles/add_article", json=(
        {
            "user_name": "string",
            "title": "string",
            "description": "string",
            "date": "string",
            "theme": "string",
            "file_name": "string"
        }
    ))
    print(response)
    assert response.status_code == 200

def test_add_photo():
    response = client.post("/articles/add_photo")
    assert response.status_code == 200 or response.status_code == 422

def test_get_photo():
    response = client.get("/articles/get_photo")
    assert response.status_code == 200 or response.status_code == 422
