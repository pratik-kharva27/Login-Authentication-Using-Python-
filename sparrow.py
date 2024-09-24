import hashlib

def load_user_data():
    user_data = {}
    try:
        with open("user_data.txt", "r") as file:
            for line in file:
                email, password = line.strip().split(":")
                #strip methos use to remove white space in to the line 
                user_data[email] = password
    except FileNotFoundError:
        user_data = {}
    return user_data

def save_user_data(user_data):
    with open("user_data.txt", "w") as file:
        for email, password in user_data.items():
            file.write(f"{email}:{password}\n")

def register_user(user_data, email, password):
    if email in user_data:
        print("\nNote:- Email already in use. Please choose a different one.\n")
    else:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user_data[email] = hashed_password
        save_user_data(user_data)
        print(f"\nNote:- User with email '{email}' registered successfully!\n")

def login_user(user_data, email, password):
    if email in user_data:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if user_data[email] == hashed_password:
            print("\nNote:- Login successful!\n")
        else:
            print("\nNote:- Login failed. Invalid email or password.\n")
    else:
        print("\nNote:- User not found. Please register first.\n")

def reset_password(user_data, email, new_password):
    if email in user_data:
        hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
        user_data[email] = hashed_password
        save_user_data(user_data)
        print("\nNote:- Password reset successfully!\n")
    else:
        print("\nNote:- User not found. Please register first.\n")

user_data = load_user_data()
print("\n*** Login Authentication Using Python ***\n")
while True:
    print("1. Register")
    print("2. Login")
    print("3. Forgot Password")
    print("4. Exit\n")
    
    print("*** Login Authentication Using Python ***\n")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        email = input("\nEnter your email: ")
        password = input("Enter your password: ")
        register_user(user_data, email, password)

    elif choice == "2":
        email = input("\nEnter your email: ")
        password = input("Enter your password: ")
        login_user(user_data, email, password)

    elif choice == "3":
        email = input("\nEnter your email: ")
        new_password = input("Enter your new password: ")
        reset_password(user_data, email, new_password)

    elif choice == "4":
        print("\n*** Exit From Authentication System ***")
        print("\n*** THANK YOU SO MUCH ***\n")
        break
