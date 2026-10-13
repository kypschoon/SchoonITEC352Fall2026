#Kyp Schoon
#01OCT2026

#Kyp Schoon
#13OCT2026
#Updated main.py for OOP to SQLite persistence
#Reuses the Snake subclasses, grows them, saves to SQLite, then displays all stored records

from objects_schoon import Snake, Boidae, Elapidae, Viperidae
from database import create_connection, create_table, insert_record, get_all_records

def main():
    # Instantiates the snake objects using the subclasses (sample data)
    anaconda = Boidae("Anaconda", "Jungle", 15, False)
    cobra = Elapidae("Cobra", "Desert", 6, True)
    cottonmouth = Viperidae("Cottonmouth", "Swamp", 4, True)

    snakes = [anaconda, cobra, cottonmouth]

    print("My snake collection:")
    # Call the methods (grow each snake)
    for snake in snakes:
        snake.grow_snake()
    print()

    # Connect to database, create table if needed, insert the (possibly grown) objects
    conn = create_connection()
    create_table(conn)
    for snake in snakes:
        insert_record(conn, snake)
    print("Objects saved to database.")

    # Retrieve and display all stored records (including any from previous runs)
    print("\nAll saved snakes from database:")
    for row in get_all_records(conn):
        # row: (snakeID, name, family, location, length, is_venomous, family_trait_1, family_trait_2)
        venomous_text = "venomous" if row[5] else "not venomous"
        print(f"ID {row[0]}: {row[1]} ({row[2]}) is a {row[4]}-foot {row[3]} snake and is {venomous_text}.")
        print(f"  Family Trait 1: {row[6]}  |  Family Trait 2: {row[7]}")
        
    conn.close()

if __name__ == "__main__":
    main()
