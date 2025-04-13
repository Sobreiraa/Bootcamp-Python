import requests
from pydantic import BaseModel

'''
requests.get # select

requests.post # create

requests.put # update

requests.delete # delete
'''

class PokemonSchame(BaseModel): # Contrato de dados, schema de dados, view da API
    name: str
    type: str

    class Config:
        from_attributes = True


def pegar_pokemon(id: int) -> PokemonSchame:
        URL = f'https://pokeapi.co/api/v2/pokemon/{id}'
        response = requests.get(URL)
        data = response.json()
        data_types = data['types']
        types_list = []
        for type_info in data_types:
            types_list.append(type_info['type']['name'])
        types = ', '.join(types_list)
        return PokemonSchame(name=data['name'], type=types)


if __name__ == "__main__":
     print(pegar_pokemon(12))
     print(pegar_pokemon(26))
     print(pegar_pokemon(25))
     print(pegar_pokemon(30))