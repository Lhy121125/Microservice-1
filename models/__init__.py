from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from.user_model import User
from.company_model import Company
from.job_model import Job
from.application_model import Application
