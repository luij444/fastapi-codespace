from pydantic import BaseModel

class User(BaseModel):
    id: int = None
    nombre: str
    apellido: str