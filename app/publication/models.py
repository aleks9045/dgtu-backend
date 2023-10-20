from sqlalchemy import Column, MetaData, Integer, String, Text, TIMESTAMP

from app.database import Base

metadata = MetaData()


class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True)
    user_name = Column(String(255), unique=True, nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    date = Column(TIMESTAMP)
    theme = Column(String(255))
