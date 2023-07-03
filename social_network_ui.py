# You can implement user interface functions here.

def loginMenu():
    print("")
    print("1. Create a new account")
    print("2. Login")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Manage my friends")
    print("3. View my messages")
    print("4. Logout")
    return input("Please Choose a number: ")

def editDetailsMenu():
    print("")
    print("1. Edit name")
    print("2. Edit age")
    print("3. Edit favorite color")
    print("4. Edit favorite animal")
    print("5. <- Go back")
    return input("Please Choose a number: ")

def manageFriendsMenu():
    print("")
    print("1. Add a friend")
    print("2. View all my friends")
    print("3. View blocked friends")
    print("4. <- Go back")
    return input("Please choose a number: ")