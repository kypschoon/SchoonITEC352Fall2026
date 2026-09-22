#Kyp Schoon
#14SEP2026

#Main function which instantiates a snake using the Snake class
#Passes in parameters to use for the attributes
#Calls both methods
from objects_schoon import Snake

def main():
    # Instantiate a Snake object
    python = Snake("Python", "Jungle", 10, False)
    cobra = Snake("Cobra", "Desert", 6, True)
    cottonmouth = Snake("Cottonmouth", "Swamp", 4, True)

    print("My snake collection:")
    # Call the methods
    python.grow_snake()
    cobra.grow_snake()
    cottonmouth.grow_snake()
    print(python.get_summary())
    print(cobra.get_summary())
    print(cottonmouth.get_summary())

if __name__ == "__main__":
    main()