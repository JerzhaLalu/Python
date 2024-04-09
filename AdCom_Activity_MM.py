user_accounts = []

def registration(user_accounts):
    print("\nRegistration")

    while True:
        username = input("\nEnter Username: ")
        if not username:
            return

        if username in user_accounts:
            print("\nUsername already in use. Please choose another.")
            continue

        password = input("Enter password: ")

        while len(password) < 5:
            print("Password should be 5 or more characters long. Try again.")
            password = input("Enter password: ")

        confirmpassword = input("Confirm password: ")

        if confirmpassword == password:
            user_accounts[username] = {"Password": password}
            print("Registration Successful!")
            sign_in(user_accounts)
        else:
            print("Passwords do not match. Please try again.")
            continue


def sign_in(user_accounts):
    print("\nSign in")

    while True:
        username = input("Username: ")
        if not username:
            return

        if username in user_accounts:
            password = input("Password: ")

            if user_accounts.get(username)["Password"] == password:
                print("Sign in successful")
                user_menu(user_accounts, username)
                break
            else:
                print("Incorrect password")
        else:
            print("Username not found")


def user_menu(user_accounts, username):
    while True:
        print("\nUser Menu")
        print("[1] Make your profile")
        print("[2] Matchmake")
        print("[3] Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            make_profile(user_accounts, username)
        elif choice == '2':
            matchmaking(user_accounts, username)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


def make_profile(user_accounts, username):
    print("\nMake Your Profile\n")

    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender (Male/Female): ")
    interests = input("Enter your interests (comma-separated): ").split(',')

    user_accounts[username]["Name"] = name
    user_accounts[username]["Age"] = age
    user_accounts[username]["Gender"] = gender
    user_accounts[username]["Interests"] = interests

    print("\nProfile updated successfully!")


def matchmaking(user_accounts, username):
    matches = []

    for user, data in user_accounts.items():
        if user != username:
            common_interests = set(user_accounts[username]["Interests"]) & set(data.get("Interests", []))
            if common_interests:
                matches.append((user, common_interests))

    print("\nMatches:")
    for match, interests in matches:
        print(f"{match} has common interests: {', '.join(interests)}")


def main():
    user_accounts = {}

    while True:
        print("\n- Main Menu -")
        print("[1] Register")
        print("[2] Sign In")
        print("[3] Exit")

        choice = input("Your choice: ")

        if choice == '1':
            registration(user_accounts)
        elif choice == '2':
            sign_in(user_accounts)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


main()
