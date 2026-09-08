"""Password Strength Audit starter template.

Complete each TODO. Do not change the required function names or parameters.
"""


def get_password_count():
    """Prompt until the user enters a positive whole number; return that number."""
    # TODO: Create a loop so the user can try again after invalid input.
    # TODO: Use try/except ValueError around the int() conversion.
    # TODO: Return only a number greater than zero.
    pass


def evaluate_password(password):
    """Return Strong, Moderate, or Weak after examining one password."""
    # TODO: Create local variables that track uppercase, lowercase, digit,
    # and special-character requirements.
    # TODO: Use a loop to inspect every character in password.
    # Hint: character.isupper(), character.islower(), and character.isdigit()
    # may be useful.
    # TODO: Count how many character-type requirements were met.
    # TODO: Use if/elif/else to return the correct rating.
    pass


def display_summary(strong_count, moderate_count, weak_count):
    """Display the totals for each password-rating category."""
    # TODO: Print a labeled final summary using the three parameters.
    pass


def main():
    """Coordinate the password audit."""
    # TODO: Create local counters for Strong, Moderate, and Weak passwords.
    # TODO: Call get_password_count().
    # TODO: Loop once for each password, call evaluate_password(), and update
    # the appropriate counter using if/elif/else.
    # TODO: Call display_summary() after the loop.
    pass


if __name__ == "__main__":
    main()
