users = {
    "user1" : "password1",
    "user2" : "password2",
    "user3" : "password3"}


def accept_login(users, username, password):
    if username in users:
        if password == users[username]:
            return True
    return False


def login():
    while True:
        if input("Do you want to sign in?\n(Y/n) ").lower() == "y":
            username = input("What is your username? ")
            password = input("And your password? ")
            if accept_login(users, username, password):
                print("login successful!")
                break
            else:
                print("login failed...")
        else:
            if input("Do you want to sign up?\n(Y/n) ").lower() == "y":
                username_input = input("Please enter your username.\n> ")
                while username_input in users:
                    username_input = input("Please use another username!\n> ")
                password_input = input("Great! That username works. Now enter your password!\n> ")
                users.update({username_input: password_input})
                print("Your username: {} was added.".format(username_input))
            else:
                print("Goodbye!")
                break




if __name__ == "__main__":
    login()
