import mysql.connector
from db_config import config

conn = mysql.connector.connect(**config)

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS types (
    type_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    type_name VARCHAR(50) NOT NULL UNIQUE
);
""")
print("TYPE TABLE SUCCESSFULLY CREATED")

cursor.execute("""
CREATE TABLE IF NOT EXISTS type_effectiveness (
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
CREATE TABLE IF NOT EXISTS pokemon (
    pokemon_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
    type1_id INT NOT NULL,
    type2_id INT,
    FOREIGN KEY (type1_id) REFERENCES types(type_id),
    FOREIGN KEY (type2_id) REFERENCES types(type_id)
);
""")
print("POKEMON TABLE SUCCESSFULLY CREATED")

cursor.execute("""
CREATE TABLE IF NOT EXISTS trainers (
    trainer_id INT PRIMARY KEY AUTO_INCREMENT,
    trainer_name VARCHAR(50) NOT NULL
);
""")
print("TRAINERS TABLE SUCCESSFULLY CREATED")

cursor.execute("""
CREATE TABLE IF NOT EXISTS trainer_pokemon (
    trainer_id INT,
    pokemon_id INT,
    slot INT CHECK (slot BETWEEN 1 AND 6),
    PRIMARY KEY (trainer_id, slot),
    FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id),
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id)
);
""")
print("TRAINER'S POKEMONS TABLE SUCCESSFULLY CREATED")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pokemon_stats (
    pokemon_id INT PRIMARY KEY,
    hp INT,
    attack INT,
    defense INT,
    speed INT,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id)
);
""")
print("POKEMON STATS TABLE SUCCESSFULLY CREATED")

conn.close()
