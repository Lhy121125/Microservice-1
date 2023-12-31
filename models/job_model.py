from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Job(Base):
    __tablename__ = "jobs"
    id: int = Column(Integer, ForeignKey("applications.job_id", ondelete='CASCADE'), primary_key=True, index=True)
    company_id: int = Column(Integer, primary_key=True, index=True)
    job_title: str = Column(String, nullable=False, unique=True)
    department: str = Column(String, nullable=False, unique=False)
    location: str = Column(String, nullable=False, unique=False)
    employment_type: str = Column(String, nullable=False, unique=False)
    description: str = Column(String, nullable=False, unique=False)
    requirements: str = Column(String, nullable=False, unique=False)
    
    company = relationship("Company", cascade="all, delete", passive_deletes=True)

    def as_dict(self):
        return {
            "id": self.id,
            "company_id":self.company_id,
            "job_title": self.job_title,
            "department": self.department,
            "location": self.location,
            "employment_type": self.employment_type,
            "description": self.description,
            "requirements": self.requirements,
        }