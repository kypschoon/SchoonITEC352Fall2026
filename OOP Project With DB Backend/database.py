import sqlite3

def create_connection():
    return sqlite3.connect("snakes.db")

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS snakes (
        snakeID INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        family TEXT NOT NULL,
        location TEXT NOT NULL,
        length INTEGER NOT NULL,
        is_venomous INTEGER NOT NULL,
        family_trait_1 TEXT,
        family_trait_2 TEXT
    )
    """)
    conn.commit()
    cursor.close()

def insert_record(conn, obj):
    cursor = conn.cursor()
    venomous_int = 1 if obj.is_venomous else 0
    family_name = type(obj).__name__          # Boidae, Elapidae, or Viperidae
    family = getattr(obj, "family_trait", "")
    parts = [p.strip() for p in family.split(",")] if family else ["", ""]
    trait_one = parts[0] if len(parts) > 0 else ""
    trait_two = parts[1] if len(parts) > 1 else ""
    cursor.execute(
        """INSERT INTO snakes 
           (name, family, location, length, is_venomous, family_trait_1, family_trait_2) 
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (obj.name, family_name, obj.location, obj.length, venomous_int, trait_one, trait_two)
    )
    conn.commit()
    cursor.close()

def get_all_records(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM snakes")
    rows = cursor.fetchall()
    cursor.close()
    return rows