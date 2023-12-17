from sqlalchemy import Column, Integer, String
from . import Base

class Application(Base):
    __tablename__ = "applications"
    company_id: int = Column(Integer, primary_key=True, index=True)
    job_id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, primary_key=True, index=True)
    time_applied: str = Column(String, nullable=False, unique=False)
    application_status: str = Column(String, nullable=False, unique=False)

    def as_dict(self):
        return {
            "company_id":self.company_id,
            "job_id": self.job_id,
            "user_id": self.user_id,
            "time_applied": self.time_applied,
            "application_status": self.application_status,
        }