import datetime
from pydantic import BaseModel, Field


class Schema(BaseModel):
    input_start: datetime.datetime = Field(..., alias="input_start")

    class Config:
        arbitrary_types_allowed = True
