import mysql.connector
from db_config import config

types = [
    'Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice',
    'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic',
    'Bug', 'Rock', 'Ghost', 'Dragon'
]

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    for type_name in types:
        cursor.execute("""
            INSERT INTO types (type_name)
            VALUES (%s)
            ON DUPLICATE KEY UPDATE type_name = type_name;
        """, (type_name,))

    conn.commit()
    print("Gen 1 Pokémon types inserted successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
