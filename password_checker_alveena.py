def check_password_strength(password):
    score = 0
    
    # Check length
    if len(password) >= 8:
        score += 1
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    
    # Check for numbers
    if any(char.isdigit() for char in password):
        score += 1
    
    # Check for special symbols
    symbols = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    if any(char in symbols for char in password):
        score += 1
    
    # Display result
    if score <= 1:
        return "WEAK  - Add more characters, numbers, and symbols"
    elif score == 2 or score == 3:
        return "MEDIUM  - Getting better! Add more variety"
    else:
        return "STRONG  - Excellent password!"

# Main program
password = input("Enter a password to check: ")
result = check_password_strength(password)
print("Password Strength:", result)