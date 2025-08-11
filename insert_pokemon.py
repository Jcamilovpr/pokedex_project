import mysql.connector
from db_config import config
import json


def get_type_id(type_name, cursor):
    if type_name is None:
        return None
    cursor.execute(
        "SELECT type_id FROM types WHERE type_name = %s;", (type_name,))
    result = cursor.fetchone()
    return result[0] if result else None


# Use the JSON that correponds to the generation
with open("data/pokedex_gen1.json", "r", encoding="utf-8") as f:
    pokemons_gen1 = json.load(f)

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    for pokemon in pokemons_gen1:
        type1_id = get_type_id(pokemon["type1"], cursor)
        type2_id = get_type_id(pokemon["type2"], cursor)

        cursor.execute("""
            INSERT INTO pokemon (pokemon_id, name, type1_id, type2_id)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                name = VALUES(name),
                type1_id = VALUES(type1_id),
                type2_id = VALUES(type2_id);
        """, (pokemon["id"], pokemon["name"], type1_id, type2_id))

        stats = pokemon["stats"]
        cursor.execute("""
            INSERT INTO pokemon_stats (pokemon_id, hp, attack, defense, speed, at_esp, def_esp)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                hp = VALUES(hp),
                attack = VALUES(attack),
                defense = VALUES(defense),
                speed = VALUES(speed),
                at_esp = VALUES(at_esp),
                def_esp = VALUES(def_esp);
        """, (pokemon["id"], stats["hp"], stats["attack"], stats["defense"], stats["speed"], stats["at_esp"], stats["def_esp"]))

    conn.commit()
    print("All Pokémon inserted successfully.")

except mysql.connector.Error as err:
    print(f"Error creating tables: {err}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
