import random
import string
import secrets

def generate_password(length=12, uppercase=True, lowercase=True, numbers=True, special_characters=True):
    characters = ''
    
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_characters:
        characters += string.punctuation
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length_range=(12, 16), **kwargs):
    passwords = []
    for _ in range(num_passwords):
        length = random.randint(length_range[0], length_range[1])
        password = generate_password(length, **kwargs)
        passwords.append(password)
    return passwords

if __name__ == "__main__":

    num_passwords = int(input("Enter the number of passwords to generate: "))
    min_length = int(input("Enter the minimum password length: "))
    max_length = int(input("Enter the maximum password length: "))
    
    generated_passwords = generate_multiple_passwords(
        num_passwords, length_range=(min_length, max_length),
        uppercase=True, lowercase=True, numbers=True, special_characters=True
    )
    
    print("\nGenerated Passwords:")
    for i, password in enumerate(generated_passwords, start=1):
        print(f"Password {i}: {password}")
