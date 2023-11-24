from pydantic import BaseModel

class MessageCreate(BaseModel):
    message: str

class MessageResponse(BaseModel):
    id: int
    message: str