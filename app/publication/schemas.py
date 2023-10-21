from pydantic import BaseModel


class article_schema(BaseModel):
    user_name: str
    title: str
    description: str
    date: str
    theme: str
    file_name: str
