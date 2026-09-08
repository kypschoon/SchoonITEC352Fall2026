# Kyp Schoon_08SEP2026

# This function prompts the user for the number of passwords they will enter and ensures that the input is a valid positive integer.
def get_password_count():
    # This loop continues to prompt the user until a valid number of passwords is entered.
    while True:
        try:
            password_count = int(input("How many passwords will you enter? "))
            if password_count <= 0:
                print("Please enter a number greater than zero.")
            else:
                return password_count
        except ValueError:
            print("Please enter a valid number.")

# This function evaluates the strength of a given password based on specific criteria, including length and character variety.
def evaluate_password(password):
    #This section initializes boolean flags to track the presence of different character types in the password.
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    #This loop iterates through each character in the password, updating the boolean flags based on the character's type.
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    #This section calculates the total number of character types present in the password.
    type_total = sum([has_uppercase, has_lowercase, has_digit, has_special])
    if password and len(password) >= 12 and type_total == 4:
        return "Strong"
    elif password and len(password) >= 8 and type_total >= 3:
        return "Moderate"
    else:
        return "Weak"


# This function displays a summary of the counts of strong, moderate, and weak passwords.
def display_summary(strong_count, moderate_count, weak_count):
    print("\nPassword Strength Summary:")
    print(f"Strong: {strong_count}")
    print(f"Moderate: {moderate_count}")
    print(f"Weak: {weak_count}")
    

# This is the main function that orchestrates the password auditing process. It collects user input, evaluates each password, 
# and displays a summary of the results.
def main():
    #This section initializes counters for the number of strong, moderate, and weak passwords entered by the user.
    strong_count = 0
    moderate_count = 0
    weak_count = 0

    # This line calls the get_password_count() function to determine how many passwords the user will enter.
    password_count = get_password_count()

    # This loop iterates for the number of passwords specified by the user, prompting for each password and evaluating its strength.
    #  The appropriate counter is incremented based on the evaluation result.
    for _ in range(password_count):
        password = input("Enter a password: ")
        rating = evaluate_password(password)
        if rating == "Strong":
            strong_count += 1
        elif rating == "Moderate":
            moderate_count += 1
        else:
            weak_count += 1

    # This line calls the display_summary() function to print the final counts of strong, moderate, and 
    # weak passwords after all passwords have been evaluated.
    display_summary(strong_count, moderate_count, weak_count)

# This conditional statement checks if the script is being run directly and calls the main() function to start the program.
if __name__ == "__main__":
    main()
