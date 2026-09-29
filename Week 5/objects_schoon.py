#Kyp Schoon
#14SEP2026

#Using dataclasses instead of hard coding __init__
from dataclasses import dataclass

#Defining the Snake class with 4 attributes and 2 methods
@dataclass
class Snake:
    name: str
    location: str
    length: int
    is_venomous: bool

    #Method that grows the snake by a certain number of feet 
    def grow_snake(self):
        while True:
            try:
                feet = int(input(f"Enter the number of feet to grow {self.name}: "))
                if feet <= 0:
                    raise ValueError
                self.length += feet
                print(f"{self.name} has grown by {feet} feet.")
                break
            except ValueError:
                print("The number of feet must be a positive integer. Please try again.")
        

    #Method that returns a description of the snake
    def get_summary(self):
        return (f"{self.name} is a {self.length}-foot {self.location} snake and is {'venomous' if self.is_venomous else 'not venomous'}.")

    def __str__(self):
        return self.get_summary()

# Defines subclass Viperidae and adds family trait
@dataclass
class Viperidae(Snake):
    family_trait: str = "Hinged Fangs, Hemotoxic Venom"

    def get_summary(self):
        return (f"{self.name} is a {self.length}-foot {self.location} Snake in the Viperidae family and is venomous. Family trait: {self.family_trait}.")


@dataclass
class Boidae(Snake):
    family_trait: str = "Constrictor, Live Birth"

    def get_summary(self):
        return (f"{self.name} is a {self.length}-foot {self.location} Snake in the Boidae Family and is not venomous. Family trait: {self.family_trait}.")


@dataclass
class Elapidae(Snake):
    family_trait: str = "Fixed Fangs, Neurotoxic Venom"

    def get_summary(self):
        return (f"{self.name} is a {self.length}-foot {self.location} Snake in the Elapidae family and is venomous. Family trait: {self.family_trait}.")