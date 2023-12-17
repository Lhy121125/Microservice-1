import strawberry
from scalars.application_scalar import AddApplication, ApplicationDeleted, ApplicationExists, ApplicationIdMissing, ApplicationNotFound


AddApplicationResponse = strawberry.union("AddApplicationResponse", (AddApplication, ApplicationExists))
DeleteApplicationResponse = strawberry.union("DeleteApplicationResponse", (ApplicationDeleted,ApplicationNotFound, ApplicationIdMissing))