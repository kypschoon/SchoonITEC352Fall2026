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

    snakes = [anaconda, cobra, cottonmouth]

    print("My snake collection:")
    # Call the methods
    for snake in snakes:
        snake.grow_snake()
    print()

    # Prints the summary of each snake using the snake object and calls the def __str__ method and shows polymorphism
    for snake in snakes:
        print(snake, end="\n\n")

if __name__ == "__main__":
    main()