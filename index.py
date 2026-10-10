
import secrets

print("==============================")
print("   NUMBER PASSWORD GENERATOR")
print("==============================")

while True:
    user_input = input("Enter password length (8-64): ")

    if not user_input.isdigit():
        print("Error: Please enter numbers only!")
        continue

    length = int(user_input)

    if length < 8 or length > 64:
        print("Error: Length must be between 8 and 64!")
        continue

    password = ''.join(
        str(secrets.randbelow(10))
        for _ in range(length)
    )

    print("Your password:", password)
    break
