"""
Example of object oriented class called Garden for ITEC-352-001
main routine included with OOP code
Sharon Gumina
9/10/2026
"""""

#Using dataclasses instead of hard coding __init__
from dataclasses import dataclass

#Defining the Garden class with 4 attributes and 2 methods
@dataclass
class Garden:
    name: str
    location: str
    plant_count: int
    has_irrigation: bool

    #Method that accepts and prints out the number of plants to plant
    def grow_plants(self, number):
        """Adds newly planted plants to the garden."""
        if number > 0:
            self.plant_count += number
            print(f"{number} plants were added to {self.name}.")
        else:
            print("Enter a positive number of plants.")

    #Method that returns a description of the garden
    def get_summary(self):
        """Returns a description of the garden."""
        irrigation_status = "has irrigation" if self.has_irrigation else "does not have irrigation"

        return (
            f"{self.name} is located at {self.location}. "
            f"It has {self.plant_count} plants and {irrigation_status}."
        )

