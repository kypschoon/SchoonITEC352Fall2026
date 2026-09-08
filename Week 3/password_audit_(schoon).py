"""Password Strength Audit starter template.

Complete each TODO. Do not change the required function names or parameters.
"""

# TODO: Create a loop so the user can try again after invalid input.
# TODO: Use try/except ValueError around the int() conversion.
# TODO: Return only a number greater than zero.
def get_password_count():
    """Prompt until the user enters a positive whole number; return that number."""
    while True:
        try:
            password_count = int(input("How many passwords will you enter? "))
            if password_count <= 0:
                print("Please enter a number greater than zero.")
            else:
                return password_count
        except ValueError:
            print("Please enter a valid number.")


 # TODO: Create local variables that track uppercase, lowercase, digit,
    # and special-character requirements.
    # TODO: Use a loop to inspect every character in password.
    # Hint: character.isupper(), character.islower(), and character.isdigit()
    # may be useful.
    # TODO: Count how many character-type requirements were met.
    # TODO: Use if/elif/else to return the correct rating.
def evaluate_password(password):
    """Return Strong, Moderate, or Weak after examining one password."""
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    type_total = sum([has_uppercase, has_lowercase, has_digit, has_special])
    if password and len(password) >= 12 and type_total == 4:
        return "Strong"
    elif password and len(password) >= 8 and type_total >= 3:
        return "Moderate"
    else:
        return "Weak"



# TODO: Print a labeled final summary using the three parameters.
def display_summary(strong_count, moderate_count, weak_count):
    """Display the totals for each password-rating category."""
    print("\nPassword Strength Summary:")
    print(f"Strong: {strong_count}")
    print(f"Moderate: {moderate_count}")
    print(f"Weak: {weak_count}")
    


def main():
    """Coordinate the password audit."""
    # TODO: Create local counters for Strong, Moderate, and Weak passwords.
    strong_count = 0
    moderate_count = 0
    weak_count = 0

    # TODO: Call get_password_count().
    password_count = get_password_count()

    # TODO: Loop once for each password, call evaluate_password(), and update
    # the appropriate counter using if/elif/else.
    for _ in range(password_count):
        password = input("Enter a password: ")
        rating = evaluate_password(password)
        if rating == "Strong":
            strong_count += 1
        elif rating == "Moderate":
            moderate_count += 1
        else:
            weak_count += 1

    # TODO: Call display_summary() after the loop.
    display_summary(strong_count, moderate_count, weak_count)


if __name__ == "__main__":
    main()
