#Kyp Schoon
#01OCT2026

#Main function which instantiates a snake using the Snake class and sublasses
#Passes in parameters to use for the attributes
#Calls all methods
from objects_schoon import Snake, Boidae, Elapidae, Viperidae

def main():
    # Instantiates the snake objects using the subclasses
    anaconda = Boidae("Anaconda", "Jungle", 15, False)
    cobra = Elapidae("Cobra", "Desert", 6, True)
    cottonmouth = Viperidae("Cottonmouth", "Swamp", 4, True)


    print("My snake collection:")
    # Call the methods
    anaconda.grow_snake()
    cobra.grow_snake()
    cottonmouth.grow_snake()
    print()

    # Print the summary of each snake call the def __str__ method and shows polymorphism
    snakes = [anaconda, cobra, cottonmouth]
    for snake in snakes:
        print(snake, end="\n\n")

if __name__ == "__main__":
    main()