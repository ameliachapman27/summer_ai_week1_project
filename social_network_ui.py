# You can implement user interface functions here.

def loginMenu():
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    print("")
    print("1. Create a new account")
    print("2. Login")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("\nYou are now in the menu to manage your account")
    print("\n1. Edit my details")
    print("2. Manage my friends")
    print("3. View my messages")
    print("4. Logout")
    return input("Please Choose a number: ")

def editDetailsMenu():
    print("")
    print("\nYou are now in the menu to edit your details")
    print("\n1. Edit name")
    print("2. Edit age")
    print("3. Edit favorite color")
    print("4. Edit favorite animal")
    print("5. <- Go back")
    return input("Please Choose a number: ")

def manageFriendsMenu():
    print("")
    print("\nYou are now in the menu to manage your frienfs")
    print("\n1. Add a friend")
    print("2. View all my friends")
    print("3. Block a friend")
    print("4. <- Go back")
    return input("Please choose a number: ")