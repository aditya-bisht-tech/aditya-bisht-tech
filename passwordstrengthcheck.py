#code by using my 12 class knowledge

def password_strength_checker(password):
    # Initial conditions
    h_length = len(password) >= 8
    h_upper = any(char.isupper() for char in password)
    h_lower = any(char.islower() for char in password)
    h_digit = any(char.isdigit() for char in password)
    h_special = any(char in "@#$%^&*!" for char in password)
    
    # Calculate score based on met conditions
    consitions = [h_length, h_upper, h_lower, h_digit, h_special]
    score = sum(conditions)
    
    # Determine strength level
    if score <= 2:
        return 'weak'
    elif score in (3, 4):
        return 'medium'
    else:
        return 'strong'

# Get user input and display result
user_password = input('Enter password: ')
result = password_strength_checker(user_password)
print(f"Your password is: {result}")
