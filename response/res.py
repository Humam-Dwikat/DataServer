from pydantic import BaseModel


class Success(BaseModel):
    res: dict
    msg: str


class Fail(BaseModel):
    msg: str
    error: str
