from dataclasses import dataclass

# a class with three attributes and two methods
@dataclass                           # dataclass decorator
class College:
    name:str                         # attribute 1
    PublicorPrivate:str              # attribute 2
    city:str                         # attribute 3
    state:str                        # attribute 4

    # This is a method that returns the location of the college as a string.
    def getLocation(self):
        return f"{self.city}, {self.state}"

    # This is a method that calculates tuition based on the state of the college and the student's residency status.
    def getTuition(self):
        inStateTuition = input("Do you live in the state of the college? (yes/no): ")
        if inStateTuition.lower() == "yes":
            return f"In-state tuition for {self.name} is $10,000"
        else:
            return f"Out-of-state tuition for {self.name} is $30,000"

