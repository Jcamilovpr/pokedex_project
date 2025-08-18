import mysql.connector
from db_config import config
from data.type_chart_data import type_chart

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    for attacker, defender, multiplier in type_chart:
        cursor.execute("""
        INSERT INTO type_effectiveness (attacker_type_id, defender_type_id, multiplier)
        SELECT a.type_id, d.type_id, %s
        FROM types a, types d
        WHERE a.type_name = %s AND d.type_name = %s
        ON DUPLICATE KEY UPDATE multiplier = VALUES(multiplier)
    """, (multiplier, attacker, defender))

    conn.commit()
    print("All type effectiveness data inserted successfully.")

except mysql.connector.Error as err:
    print(f"Error inserting type effectiveness data: {err}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
