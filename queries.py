import mysql.connector
from db_config import config

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.pokemon_id, p.name, t1.type_name, t2.type_name
        FROM pokemon p
        JOIN types t1 ON p.type1_id = t1.type_id
        LEFT JOIN types t2 ON p.type2_id = t2.type_id
        ORDER BY p.pokemon_id ASC;
    """)

    resultados = cursor.fetchall()
    for row in resultados:
        print(
            f"ID: {row[0]}, Name: {row[1]}, Type1: {row[2]}, Type2: {row[3]}")

    cursor.execute("""
        SELECT pokemon.name, hp, attack, defense, speed, at_esp, def_esp FROM pokemon
        JOIN pokemon_stats
        ON pokemon.pokemon_id = pokemon_stats.pokemon_id
        ORDER BY pokemon.pokemon_id ASC;
    """)

    resultados = cursor.fetchall()
    for row in resultados:
        print(
            f"Name: {row[0]}, Hp: {row[1]}, Attack: {row[2]}, Speed: {row[3]}, at_esp: {row[4]}, Def_esp: {row[5]}")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
