from sqlalchemy import Table, Column, MetaData, Integer, LargeBinary
from sqlalchemy.dialects.postgresql import BYTEA

metadata = MetaData()

file = Table(
    'file',
    metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('bfile', LargeBinary)
)
