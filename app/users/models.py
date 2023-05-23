from sqlalchemy import Integer, Column, String
from app.database import Base


class Users(Base):
    def __init__(self, **kw: Any):
        super().__init__(kw)
        self.role = None

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
