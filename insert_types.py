import mysql.connector
from db_config import config

# write the types you dont have in your database
types = [
    (1, "Normal"), (2, "Fire"), (3, "Water"),
    (4, "Electric"), (5, "Grass"), (6, "Ice"),
    (7, "Fighting"), (8, "Poison"), (9, "Ground"),
    (10, "Flying"), (11, "Psychic"), (12, "Bug"),
    (13, "Rock"), (14, "Ghost"), (15, "Dragon"),
    (16, "Dark"), (17, "Steel"), (18, "Fairy")
]

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    for type_id, type_name in types:
        cursor.execute("""
            INSERT INTO types (type_id, type_name)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE type_name = VALUES(type_name);
        """, (type_id, type_name))

    conn.commit()
    print("Gen 1 Pokémon types inserted successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
