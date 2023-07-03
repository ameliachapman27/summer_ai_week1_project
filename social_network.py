#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    last_menu = None
    choice = social_network_ui.loginMenu()

    while True: 
        #Creating an account
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        #Logging in
        elif choice == "2":
            print("")
            enteredUsername = input("Enter your username: ")
            print(SocialNetwork.listUsernames)
            print(enteredUsername)
            #if enteredUsername not in SocialNetwork.listUsernames:
                #print("There is no account with that username")
                #break
            #else: 
            manageAccount_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                
                #Editing details (task 1)
                if manageAccount_menu_choice == "1":
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
                            print("Your input is invalid. Try Again!")
                            
                        editDetails_menu_choice = social_network_ui.editDetailsMenu()

                #Adding, viewing, & blocking friends (tasks 2, 3, & 4)
                elif manageAccount_menu_choice == "2":
                    manageFriends_menu_choice = social_network_ui.manageFriendsMenu()
                    while True:
                        if manageFriends_menu_choice == "1":
                            addedFriend = input("Enter the name of the friend you would like to add: ")
                            p1.friendList.append(addedFriend)
                            print(p1.friendList)
                            break
                        
                        #Viewing friends
                        elif manageFriends_menu_choice == "2":
                            print(p1.friendList)

                        #Block a friend
                        elif manageFriends_menu_choice == "3":
                            print (f"Here is a list of your current friends: {p1.friendList}")
                            badFriend = input("Which friend would you like to block? ")
                            if badFriend in p1.friendList: 
                                p1.remove(badFriend)
                                print(f"{badFriend} has been removed from your friends list")
                            else:
                                print("The friend you entered is not in your friends list. Please try again")
                            break

                        #Going back
                        elif manageFriends_menu_choice == "4":
                            break

                        else:
                            print("Your input is invalid. Try Again!")
                            
                        manageFriends_menu_choice = social_network_ui.manageFriendsMenu()
                
                #Sending & viewing messages (tasks 5 & 6)
                #elif manageAccount_menu_choice == "3":


                elif manageAccount_menu_choice == "4":
                   break
                
                else: 
                    print("Your input is invalid. Try Again!")

                manageAccount_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye forever :(")
            break

        else:
            print("Your input is invalid. Try Again!")
    
        #restart menu
        choice = social_network_ui.loginMenu()



        
