import random
import string

def generate_password(password_type, length):
    if password_type == 1:
        characters = string.ascii_letters + string.digits
    elif password_type == 2:
        characters = string.ascii_letters
    elif password_type == 3:
        characters = string.digits
    elif password_type == 4:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid password type")

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Types of passwords:")
    print("1 - Numbers and letters")
    print("2 - Only letters")
    print("3 - Only numbers")
    print("4 - Numbers, letters, and symbols")

    password_type = int(input("Enter the number corresponding to the password type: "))
    length = int(input("Enter the length of the passwords: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))

    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        password = generate_password(password_type, length)
        print(password)

if __name__ == "__main__":
    main()
