from sqlalchemy import Column, Integer, String, ForeignKey
from . import Base

class User(Base):
    __tablename__ = "users"
    id: int = Column(Integer, ForeignKey("applications.user_id", ondelete='CASCADE'), primary_key=True, index=True)
    email: str = Column(String, nullable=False, unique=True)
    name: str = Column(String, nullable=False, unique=False)
    school: str = Column(String, nullable=False, unique=False)
    role: str = Column(String, nullable=False, unique=False)
    additional_information: str = Column(String, nullable=False, unique=False)

    def as_dict(self):
        return {
            "id": self.id,
            "email":self.email,
            "name": self.name,
            "school": self.school,
            "role": self.role,
            "additional_information": self.additional_information
        }