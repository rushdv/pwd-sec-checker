def checkPasswordStrength(password):
    lengthError = len(password) < 8
    upperError = not any(char.isupper() for char in password)
    lowerError = not any(char.islower() for char in password)
    digitError = not any(char.isdigit() for char in password)
    specialError = not any(char in "!@#$%^&*()-_=+" for char in password)

    # errors = [lengthError, upperError, lowerError, digitError, specialError]
    # score = errors.count(False)

    score = 0

    if not lengthError:
        score += 1
    if not upperError:
        score += 1
    if not lowerError:
        score += 1
    if not digitError:
        score += 1
    if not specialError:
        score += 1


    if score <= 2:
        return "Weak Password"
    elif score == 3 or score == 4:
        return "Medium Password"
    else:
        return "Strong Password"
    
password = input("Enter your password: ")
result = checkPasswordStrength(password)

print("Password Strength: ", result)