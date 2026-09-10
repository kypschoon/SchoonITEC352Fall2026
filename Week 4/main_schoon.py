#Main function which instantiates a garden using the Garden class
#Passes in parameters to use for the attributes
#Calls both methods
from objects_gumina import Garden

def main():
    # Instantiate a Garden object
    my_garden = Garden("Sunshine Garden", "Backyard", 12, True)

    # Call the methods
    my_garden.grow_plants(5)
    print(my_garden.get_summary())

if __name__ == "__main__":
    main()