import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    password_length = int(input("Provide the password length: "))
    generated_password = generate_password(password_length)
    print(f"Generated password: {generated_password}")
except ValueError:
    print("Invalid input. Please enter a valid integer for the password length.")
