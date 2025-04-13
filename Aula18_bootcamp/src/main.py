import time
import random
from controller import fetch_pokemon_data, add_pokemon_to_db


def main():
    while True:
        pokemon_id = random.randint(1, 350)
        pokemon_schema = fetch_pokemon_data(pokemon_id)
        if pokemon_schema:
            print(f'Adicionando {pokemon_schema} ao banco de dados.')
            add_pokemon_to_db(pokemon_schema)
            time.sleep(10)
        else:
            print(f'Não foi possível obter dados apra o Pokémon com ID {pokemon_schema}')


if __name__ == "__main__":
    main()