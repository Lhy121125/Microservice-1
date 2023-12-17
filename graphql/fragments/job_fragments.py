import strawberry
from scalars.job_scalar import AddJob, JobDeleted, JobExists, JobIdMissing, JobNotFound


AddJobResponse = strawberry.union("AddJobResponse", (AddJob, JobExists))
DeleteJobResponse = strawberry.union("DeleteJobResponse", (JobDeleted,JobNotFound, JobIdMissing))