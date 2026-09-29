#Kyp Schoon
#14SEP2026

#Main function which instantiates a snake using the Snake class
#Passes in parameters to use for the attributes
#Calls both methods
from objects_schoon import Snake, Boidae, Elapidae, Viperidae

def main():
    # Instantiate a Snake object
    anaconda = Boidae("Anaconda", "Jungle", 15, False)
    cobra = Elapidae("Cobra", "Desert", 6, True)
    cottonmouth = Viperidae("Cottonmouth", "Swamp", 4, True)


    print("My snake collection:")
    # Call the methods
    anaconda.grow_snake()
    cobra.grow_snake()
    cottonmouth.grow_snake()
    print()
    snakes = [anaconda, cobra, cottonmouth]
    for snake in snakes:
        print(snake, end="\n\n")

if __name__ == "__main__":
    main()