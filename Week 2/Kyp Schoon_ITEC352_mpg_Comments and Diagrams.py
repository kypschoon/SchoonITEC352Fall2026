#!/usr/bin/env python3
#Kyp Schoon 31AUG2026

# This function prompts the user for miles driven and returns the value. It will not accept a value less than or equal to zero.
def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven

# This function prompts the user for gallons of gas used and returns the value. It will not accept a value less than or equal to zero.          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

# This function calculates and returns the miles per gallon based on the miles driven and gallons of gas used. It will ask for more entries until the user indicates they are finished. 
# It will then display a goodbye message and exit the program.
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    more = "y"
    # This while loop will continue to ask the user for miles driven and gallons of gas used until the user indicates they are finished by entering "n" when prompted.
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        # This line calculates the miles per gallon by dividing the miles driven by the gallons of gas used and rounding the result to two decimal places.                         
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()
        
        more = input("More entries? (y or n): ")
    
    print("Bye!")

# This is the main entry point of the program.
if __name__ == "__main__":
    main()

