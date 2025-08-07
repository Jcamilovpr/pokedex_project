import mysql.connector

try:
    # connect with database
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root1234",
        database="pokemon"
    )

    # Verificamos si está conectado
    if conn.is_connected():
        print("Successfully connected to the database.")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE types (
            type_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
            type_name VARCHAR(50) NOT NULL
        );
        """)
        print("TYPE TABLE SUCCESSFULLY CREATED")

        cursor.execute("""
        CREATE TABLE type_effectiveness (
            attacker_type_id INT,
            defender_type_id INT,
            multiplier DECIMAL(3,2),
            PRIMARY KEY (attacker_type_id, defender_type_id),
            FOREIGN KEY (attacker_type_id) REFERENCES types(type_id),
            FOREIGN KEY (defender_type_id) REFERENCES types(type_id)
        );
        """)
        print("TYPE EFFECTIVENESS TABLE SUCCESSFULLY CREATED")

        cursor.execute("""
        CREATE TABLE pokemon (
            pokemon_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL,
            type1_id INT NOT NULL,
            type2_id INT,
            FOREIGN KEY (type1_id) REFERENCES types(type_id),
            FOREIGN KEY (type2_id) REFERENCES types(type_id)
        );
        """)
        print("POKEMON TABLE SUCCESSFULLY CREATED")

        cursor.execute("""
        CREATE TABLE trainers (
            trainer_id INT PRIMARY KEY AUTO_INCREMENT,
            trainer_name VARCHAR(50) NOT NULL
        );
        """)
        print("TRAINERS TABLE SUCCESSFULLY CREATED")

        cursor.execute("""
        CREATE TABLE trainer_pokemon (
            trainer_id INT,
            pokemon_id INT,
            slot INT CHECK (slot BETWEEN 1 AND 6),
            PRIMARY KEY (trainer_id, slot),
            FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id),
            FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id)
        );
        """)
        print("TRAINER'S POKEMONS TABLE SUCCESSFULLY CREATED")

    else:
        print("Could not connect to the database.")

except mysql.connector.Error as err:
    print("Connection error:", err)


finally:
    # Cerramos la conexión si está abierta
    if conn.is_connected():
        conn.close()
        print("🔒 Connection closed.")
