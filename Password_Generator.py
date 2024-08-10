import random
import string

def generate_password(length, include_numbers, include_special, include_uppercase):
    
    # Initialize possible characters
    characters = string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    if include_uppercase:
        characters += string.ascii_uppercase
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
length = 12  # Length of the password
include_numbers = True  # Include numbers
include_special = True  # Include special characters
include_uppercase = True  # Include uppercase letters

password = generate_password(length, include_numbers, include_special, include_uppercase)
print("Generated Password:", password)
