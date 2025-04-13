import requests
from db import SessionLocal, engine, Base
from models import Pokemon
from schema import PokemonSchema


Base.metadata.create_all(bind=engine)


def fetch_pokemon_data(pokemon_id: int):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    if response.status_code == 200:
        data = response.json()
        type_names = []

        for type_info in data['types']:
            type_names.append(type_info['type']['name'])

        types = ', '.join(type_names)
        return PokemonSchema(name=data['name'], type=types)
    else:
        return None


def add_pokemon_to_db(pokemon_schema: PokemonSchema) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
    return db_pokemon