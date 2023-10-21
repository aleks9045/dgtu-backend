from sqlalchemy import Column, MetaData, Integer, String, Text, TIMESTAMP

from app.database import Base

metadata = MetaData()


class Article(Base):
    __tablename__ = "article"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_name = Column(String(255), nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    date = Column(TIMESTAMP)
    theme = Column(String(255))
    file_name = Column(Text)
