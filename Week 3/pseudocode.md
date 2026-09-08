# Password Strength Audit — Pseudocode

Use this logic to plan your Python program. Translate the pseudocode into Python; do not submit pseudocode as your final program.

```text
FUNCTION get_password_count()
    REPEAT
        TRY
            PROMPT user for number of passwords to audit
            CONVERT response to an integer

            IF number is greater than 0 THEN
                RETURN number
            ELSE
                DISPLAY "Please enter a whole number greater than zero."
            END IF

        CATCH ValueError
            DISPLAY "Please enter a whole number greater than zero."
        END TRY
    UNTIL a valid number is returned
END FUNCTION


FUNCTION evaluate_password(password)
    SET has_uppercase TO False
    SET has_lowercase TO False
    SET has_digit TO False
    SET has_special TO False

    FOR EACH character IN password
        IF character is uppercase THEN
            SET has_uppercase TO True
        ELSE IF character is lowercase THEN
            SET has_lowercase TO True
        ELSE IF character is a digit THEN
            SET has_digit TO True
        ELSE
            SET has_special TO True
        END IF
    END FOR

    SET type_total TO the number of True character-type variables

    IF password length is at least 12 AND type_total equals 4 THEN
        RETURN "Strong"
    ELSE IF password length is at least 8 AND type_total is at least 3 THEN
        RETURN "Moderate"
    ELSE
        RETURN "Weak"
    END IF
END FUNCTION


FUNCTION display_summary(strong_count, moderate_count, weak_count)
    DISPLAY a heading for the audit summary
    DISPLAY strong_count
    DISPLAY moderate_count
    DISPLAY weak_count
END FUNCTION


FUNCTION main()
    SET strong_count TO 0
    SET moderate_count TO 0
    SET weak_count TO 0

    SET password_count TO CALL get_password_count()

    FOR password_number FROM 1 THROUGH password_count
        PROMPT user for one password
        SET rating TO CALL evaluate_password(password)
        DISPLAY rating

        IF rating equals "Strong" THEN
            INCREASE strong_count by 1
        ELSE IF rating equals "Moderate" THEN
            INCREASE moderate_count by 1
        ELSE
            INCREASE weak_count by 1
        END IF
    END FOR

    CALL display_summary(strong_count, moderate_count, weak_count)
END FUNCTION


IF this file is being run directly THEN
    CALL main()
END IF
```

## Planning questions

Before coding, be able to answer these questions:

1. Which variables are local to `evaluate_password()`?
2. What information enters and leaves each function?
3. Why does `get_password_count()` need a loop even though `main()` already has a loop?
4. Which decision determines the final password rating?
5. What would happen if `int()` were used without `try` / `except`?
