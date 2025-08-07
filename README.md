# Pokémon SQL Project

This project models a Pokémon-themed relational database to practice SQL, data modeling, and Python integration. It includes real-world database concepts such as one-to-one, one-to-many, and many-to-many relationships.

## Project Structure

- `create_tables.py`: Creates all database tables.
- `insert_types.py`: Inserts Pokémon types (e.g., Fire, Water, Grass).
- `insert_pokemon.py`: Inserts Pokémon with their respective types.
- `insert_trainers.py`: Inserts trainers and their Pokémon teams.
- `queries.py`: Sample SQL queries for analysis and data retrieval.
- `db_config.py`: Stores the database connection configuration.
- `README.md`: Project documentation and usage guide.

## Key Concepts Practiced

- Relational data modeling
- Primary and foreign keys
- SQL joins and constraints
- One-to-one, one-to-many, many-to-many relationships
- Database interaction using Python (`mysql-connector-python`)

## How to Run the Project

1. **Set up your database**

   - Create a MySQL database named `pokemon` (or update the config).

2. **Configure the connection**

   - Edit `db_config.py` with your database credentials.

3. **Run scripts in order**
   ```bash
   python create_tables.py       # Creates all tables
   python insert_types.py        # Adds Pokémon types
   python insert_pokemon.py      # Adds Pokémon
   python insert_trainers.py     # Adds trainers and teams
   python queries.py             # Run example queries
   ```
