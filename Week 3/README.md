# Password Strength Audit — Procedural Programming Assignment

## Overview

Build a command-line Python program that audits a set of passwords and reports how many are **Strong**, **Moderate**, or **Weak**. The program is intentionally small enough to complete in one class period, but it must demonstrate the procedural-programming techniques listed below.

## Learning goals

Your completed program must demonstrate:

- modularization with functions;
- `for` and/or `while` loops;
- `if` / `elif` / `else` decisions;
- local variables within functions;
- parameter passing and return values; and
- exception handling with `try` / `except`.

## Scenario and password rules

The user first enters the number of passwords to audit. The program then prompts for that many passwords, one at a time.

Classify each password using these rules:

| Rating | Required conditions |
| --- | --- |
| Strong | At least 12 characters, at least one uppercase letter, at least one lowercase letter, at least one digit, and at least one special character. |
| Moderate | At least 8 characters and meets at least three of the four character-type requirements. |
| Weak | Any password that does not meet the Strong or Moderate rules. |

Treat any character that is not a letter or digit as a special character. A password is allowed to contain spaces, although students may choose to reject blank passwords as Weak.

## Required program structure

Start with `template.py` and rename your finished file to `password_audit.py`.

Your solution must include these functions. You may add more helper functions if useful.

1. `get_password_count()`
   - Prompts for the number of passwords to audit.
   - Uses `try` / `except ValueError` to handle non-numeric input.
   - Repeats until the user enters a positive integer.
   - Returns the valid number.

2. `evaluate_password(password)`
   - Receives one password as a parameter.
   - Uses a loop to inspect the characters.
   - Uses local Boolean variables/counters to track the password characteristics.
   - Returns the text `"Strong"`, `"Moderate"`, or `"Weak"`.

3. `display_summary(strong_count, moderate_count, weak_count)`
   - Receives the three totals as parameters.
   - Displays a readable final summary.

4. `main()`
   - Calls the other functions.
   - Uses a loop to collect and evaluate every password.
   - Maintains the three category totals.

Include the standard function call at the bottom of the program:

```python
if __name__ == "__main__":
    main()
```

## Example interaction

```text
How many passwords would you like to audit? three
Please enter a whole number greater than zero.
How many passwords would you like to audit? 3

Password 1: Summer2026!
Rating: Moderate

Password 2: C0mpl3x!Passphrase
Rating: Strong

Password 3: password
Rating: Weak

--- Password Audit Summary ---
Strong passwords:   1
Moderate passwords: 1
Weak passwords:     1
```

## Submission instructions

1. Clone this repository to your computer.
2. Complete `template.py`, then save your completed work as `password_audit.py`.
3. Test at least these cases:
   - a non-numeric password count;
   - zero or a negative count;
   - one Strong, one Moderate, and one Weak password.
4. Add a comment above each function stating its purpose.
5. Commit and push your finished `password_audit.py` to **your own GitHub repository**.
6. Submit the link to your repository as directed by your instructor.

## Academic integrity reminder

You may discuss the logic and use class resources, but the final program must be your own work. Be prepared to explain the purpose of each function, identify its local variables, and trace how the program moves from `main()` through the other functions.

## Instructor checklist

Use this quick checklist when reviewing submissions:

- [ ] At least three student-written functions (not counting the starter call).
- [ ] A loop is used to process passwords and a loop is used to inspect password characters.
- [ ] Correct `if` / `elif` / `else` classification logic.
- [ ] Meaningful local variables are used inside functions.
- [ ] Parameters and return values connect the functions.
- [ ] `try` / `except ValueError` validates the password count.
- [ ] Program runs without errors and produces a final summary.
