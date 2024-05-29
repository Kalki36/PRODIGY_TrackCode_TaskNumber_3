def password_complexity(pswd):

    upper = False
    lower = False
    digit = False
    special = False
    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"

    for char in pswd:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            digit = True
        elif char in special_chars:
            special = True

    length_score = min(10, len(pswd))
    upper_score = 10 if upper else 0
    lower_score = 10 if lower else 0
    digit_score = 10 if digit else 0
    special_score = 10 if special else 0

    total_score = length_score + upper_score + lower_score + digit_score + special_score

    return total_score

pswd = input("Enter the password to check the strength: ")
complexity = password_complexity(pswd)
print("The Strength of password is out of 50")
print("Password Complexity Feedback:", complexity)