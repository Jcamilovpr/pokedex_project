# Pokémon SQL Project

This project models a Pokémon-themed relational database to practice **SQL, relational data modeling, and Python integration**.  
It demonstrates real-world concepts such as **one-to-one, one-to-many, and many-to-many relationships**, along with advanced queries and constraints.

## Project Structure

- `create_tables.py`: Creates all database tables.
- `insert_types.py`: Inserts Pokémon types (e.g., Fire, Water, Grass).
- `insert_pokemon.py`: Inserts Pokémon with their stats and types.
- `insert_trainers.py`: Inserts trainers and their Pokémon teams.
- `queries.py`: Contains example SQL queries for analysis and data retrieval.
- `db_config.py`: Stores the database connection configuration.
- `README.md`: Project documentation and usage guide.

## Key Concepts Practiced

- Relational database modeling
- Primary keys and foreign keys
- SQL joins, subqueries, and constraints
- One-to-one, one-to-many, and many-to-many relationships
- Data validation and prevention of duplicates
- Database interaction using Python (`mysql-connector-python`)

## How to Run the Project

1. **Set up your database**

   - Create a MySQL database named `pokemon_db` (or update the name in `db_config.py`).

2. **Configure the connection**

   - Edit `db_config.py` with your database credentials:
     ```python
     config = {
         "host": "localhost",
         "user": "your_user",
         "password": "your_password",
         "database": "pokemon_db"
     }
     ```

3. **Run the scripts in order**
   ```bash
   python create_tables.py       # Creates all tables
   python insert_types.py        # Adds Pokémon types
   python insert_pokemon.py      # Adds Pokémon and stats
   python insert_trainers.py     # Adds trainers and their teams
   python queries.py             # Executes example queries
   ```
