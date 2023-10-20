from sqlalchemy import Table, Column, MetaData, Integer, String, Boolean
from app.database import Base

metadata = MetaData()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True),
    email = Column(String, nullable=False),
    name = Column(String(16), nullable=False),
    photo = Column(String, nullable=True),
    hashed_password = Column(String(length=1024), nullable=False),
    is_active = Column(Boolean, default=True, nullable=False),
    is_superuser = Column(Boolean, default=False, nullable=False),
    is_verified = Column(Boolean, default=False, nullable=False)

