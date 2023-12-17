from sqlalchemy import Column, Integer, String, ForeignKey
from . import Base
from datetime import date

class Company(Base):
    __tablename__ = "companies"
    id: int = Column(Integer, ForeignKey("jobs.company_id", ondelete='CASCADE'), primary_key=True, index=True)
    name: str = Column(String, nullable=False, unique=False)
    location: str = Column(String, nullable=False, unique=False)
    industry: str = Column(String, nullable=False, unique=False)
    inception_date: date = Column(String, nullable=False, unique=False)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "industry": self.industry,
            "inception_date": self.inception_date
        }