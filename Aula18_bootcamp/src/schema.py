from pydantic import BaseModel

class PokemonSchema(BaseModel): # Contrato de dados, schema de dados, view da API
    name: str
    type: str

    class Config:
        from_attributes = True