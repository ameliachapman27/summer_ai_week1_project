#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.loginMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            print("")
            enteredUsername = input("Enter your username: ")
            #print(social_network_classes.listUsernames)
            print(enteredUsername)
            #if enteredUsername not in SocialNetwork.__init__(listUsernames):
                #print("There is no account with that username")
                #break
            #else: 
            manageAccount_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                
                #Editing details (task 1)
                if manageAccount_menu_choice == "1":
                    print("\nYou are now in the menu to edit your details")
                    editDetails_menu_choice = social_network_ui.editDetailsMenu()
                    while True:
                        if editDetails_menu_choice == "1":
                            p1 = ai_social_network.listPeople[0]
                            p1.name = input("Enter your new name: ")
                            print("\nYour new name is",p1.name)
                            break
                        
                        elif editDetails_menu_choice == "2":
                            p1 = ai_social_network.listPeople[0]
                            p1.age = input("Enter your new age: ")
                            print("\nYour new age is",p1.age)
                            break

                        elif editDetails_menu_choice == "3":
                            p1 = ai_social_network.listPeople[0]
                            p1.favColor = input("Enter your new favorite color: ")
                            print("\nYour new favorite color is",p1.favColor)
                            break
                        
                        elif editDetails_menu_choice == "4":
                            p1 = ai_social_network.listPeople[0]
                            p1.favAnimal = input("Enter your new favorite animal: ")
                            print("\nYour new favorite animal is a",p1.favAnimal)
                            break

                        elif editDetails_menu_choice == "5":
                            break
                        else:
                            editDetails_menu_choice = social_network_ui.editDetailsMenu()

                #Adding, viewing, & blocking friends (tasks 2, 3, & 4)
                elif manageAccount_menu_choice == "2":
                    print("\nYou are now in the menu to manage your friends")
                    manageFriends_menu_choice = social_network_ui.manageFriendsMenu()
                    while True:
                        if manageFriends_menu_choice == "1":
                            addedFriend = input("Enter the name of the friend you would like to add: ")
                            social_network_classes.listUsernames.append(addedFriend)
                            break
                        
                        #Viewing friends
                        #elif manageFriends_menu_choice == "2":

                        #Viewing blocked friends
                        #elif manageFriends_menu_choice == "3":

                        #Going back
                        #elif manageFriends_menu_choice == "4":
                            #break

                        #else:
                
                #Sending & viewing messages (tasks 5 & 6)
                #elif manageAccount_menu_choice == "3":

                elif manageAccount_menu_choice == "4":
                   break
                
                else: 
                    manageAccount_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye forever :(")
            break

        else:
            print("Your input is invalid. Try Again!")
    
        #restart menu
        choice = social_network_ui.loginMenu()



        
