from pydantic import BaseModel
from datetime import datetime

class article_schema(BaseModel):
    id: int
    user_name: str
    title: str
    description: str
    date: datetime
    theme: str
