# Read user input
user_name = input()
password = input()

# Logic
while True:
    password_check = input()
    if password_check == password:
        break

# Print Output
print(f"Welcome {user_name}!")
