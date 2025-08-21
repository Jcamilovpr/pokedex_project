import requests
import json

POKEDEX = []

# Change the range por other gens
# Pokémon de la primera generación: 1 - 152
# Pokémon de la segunda generación: 152 - 252
# Pokémon de la tercera generación: 252 - 387
# Pokémon de la cuarta generación: 387 - 494
# Pokémon de la quinta generación: 494 - 650
# Pokémon de la sexta generación: 650 - 722
# Pokémon de la séptima generación: 722 - 810
# Pokémon de la octava generación: 810 - 899

for pokemon_id in range(810, 899):
    print(f"Fetching Pokémon {pokemon_id}...")
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    data = response.json()

    # Types
    type1 = data["types"][0]["type"]["name"].capitalize()
    type2 = data["types"][1]["type"]["name"].capitalize() if len(
        data["types"]) > 1 else None

    # Stats
    stats = {
        "hp": data["stats"][0]["base_stat"],
        "attack": data["stats"][1]["base_stat"],
        "defense": data["stats"][2]["base_stat"],
        "speed": data["stats"][5]["base_stat"],
        "at_esp": data["stats"][3]["base_stat"],
        "def_esp": data["stats"][4]["base_stat"]
    }

    # Pokémon dict
    pokemon = {
        "id": pokemon_id,
        "name": data["name"].capitalize(),
        "type1": type1,
        "type2": type2,
        "stats": stats
    }

    POKEDEX.append(pokemon)

# Save file (Change name for other gens)
with open("data/pokedex_gen8.json", "w", encoding="utf-8") as f:
    json.dump(POKEDEX, f, indent=4, ensure_ascii=False)

print("pokedex_gen2.json creado con éxito.")
