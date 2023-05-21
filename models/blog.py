from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text, DateTime
from config import Base


class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text())
    description = Column(Text())
    created_at = Column(DateTime())
