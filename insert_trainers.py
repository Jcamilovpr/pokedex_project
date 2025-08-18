import mysql.connector
from db_config import config
from data.trainers_data import trainers

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    for trainer in trainers:
        # Insert the trainer
        cursor.execute("""
            INSERT INTO trainers (trainer_id, trainer_name)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE trainer_name = trainer_name;
        """, (trainer["trainer_id"], trainer["name"]))

        # Get the trainer ID
        cursor.execute(
            "SELECT trainer_id FROM trainers WHERE trainer_name = %s", (trainer["name"],))
        trainer_id = cursor.fetchone()[0]

        # Insert the pokemon in the team.
        for slot, pokemon_name in enumerate(trainer["team"], start=1):
            cursor.execute("""
                INSERT INTO trainer_pokemon (trainer_id, pokemon_id, slot)
                SELECT %s, p.pokemon_id, %s
                FROM pokemon p
                WHERE p.name = %s
                ON DUPLICATE KEY UPDATE trainer_pokemon.pokemon_id = VALUES(pokemon_id);
            """, (trainer_id, slot, pokemon_name))

    conn.commit()
    print("All trainers and their teams inserted successfully.")

except mysql.connector.Error as err:
    print(f"Error inserting trainers: {err}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
