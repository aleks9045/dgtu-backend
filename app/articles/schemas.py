from pydantic import BaseModel, Field
from fastapi import UploadFile, File


class file_schema(BaseModel):
    id: int
    name: str
    info: str
    number: int