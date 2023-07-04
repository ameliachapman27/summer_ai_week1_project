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
            currentUser = ai_social_network.listUsernames.index(enteredUsername)

            if enteredUsername not in ai_social_network.listUsernames:
                print("There is no account with that username. Please try again.")
                print("")

            else: 
                #Handle inner menu here
                while True:
                    manageAccount_menu_choice = social_network_ui.manageAccountMenu()
                    p1 = ai_social_network.listPeople[currentUser]
                    #Editing details (task 1)
                    if manageAccount_menu_choice == "1":
                        print("")
                        print("\nYou are now in the menu to edit your details")
                        print(f"\nHello, {p1.name}. Here are your current details: you are {p1.age} years old, your favorite color is {p1.favColor}, and your favorite animal is a {p1.favAnimal}.")
                        editDetails_menu_choice = social_network_ui.editDetailsMenu()
                        while True:
                            if editDetails_menu_choice == "1":
                                #p1 = ai_social_network.listPeople[currentUser]
                                p1.name = input("Enter your new name: ")
                                print("\nYour new name is",p1.name)
                                break
                            
                            elif editDetails_menu_choice == "2":
                                #p1 = ai_social_network.listPeople[currentUser]
                                p1.age = input("Enter your new age: ")
                                print("\nYour new age is",p1.age)
                                break

                            elif editDetails_menu_choice == "3":
                                #p1 = ai_social_network.listPeople[currentUser]
                                p1.favColor = input("Enter your new favorite color: ")
                                print("\nYour new favorite color is",p1.favColor)
                                break
                            
                            elif editDetails_menu_choice == "4":
                                #p1 = ai_social_network.listPeople[currentUser]
                                p1.favAnimal = input("Enter your new favorite animal: ")
                                print("\nYour new favorite animal is a",p1.favAnimal)
                                break

                            elif editDetails_menu_choice == "5":
                                break
                            
                            else:
                                print("\nYour input is invalid. Try Again!")
                                
                            editDetails_menu_choice = social_network_ui.editDetailsMenu()

                    #Adding, viewing, & blocking friends (tasks 2, 3, & 4)
                    elif manageAccount_menu_choice == "2":
                        manageFriends_menu_choice = social_network_ui.manageFriendsMenu()
                        while True:
                            if manageFriends_menu_choice == "1":
                                possibleFriends = ai_social_network.listUsernames
                                #Lines 82-83 was messing things up for some reason so I just commented it out
                                #if enteredUsername in possibleFriends:
                                    #possibleFriends.remove(ai_social_network.listUsernames[currentUser])

                                if len(possibleFriends) == 0:
                                    print("\nThere are other users to be added")
                                else:
                                    print(f"The usernames of possible friends to be added are:{possibleFriends}")
                                    addedFriend = input("Enter the name of the friend you would like to add: ")
                                    if addedFriend in p1.friendList:
                                        print(f"{addedFriend} is already in your friend list")
                                    elif addedFriend not in possibleFriends:
                                        print(f"{addedFriend} is not one of the possible friends that can be added")
                                    elif addedFriend == p1.username:
                                        print("You cannot add yourself as a friend")
                                    else:
                                        p1.friendList.append(addedFriend)
                                        print(f"Your updated friend list is: {p1.friendList}")
                                break
                            
                            #Viewing friends
                            elif manageFriends_menu_choice == "2":
                                if len(p1.friendList) == 0:
                                    print("\nYou do not have any friends added")
                                else:
                                    print(f"Your current friend list is: {p1.friendList}")
                                break

                            #Block a friend
                            elif manageFriends_menu_choice == "3":
                                if len(p1.friendList) == 0:
                                    print("\nYou do not have any friends added so you cannot block someone")
                                else:
                                    print (f"Here is a list of your current friends: {p1.friendList}")
                                    badFriend = input("Which friend would you like to block? ")
                                    if badFriend in p1.friendList: 
                                        p1.friendList.remove(badFriend)
                                        print(f"{badFriend} has been removed from your friends list")
                                    else:
                                        print("The friend you entered is not in your friends list. Please try again")
                                break

                            #Going back
                            elif manageFriends_menu_choice == "4":
                                break

                            else:
                                print("\nYour input is invalid. Try Again!")
                                
                            manageFriends_menu_choice = social_network_ui.manageFriendsMenu()
                    
                    #Sending & viewing messages (tasks 5 & 6)
                    elif manageAccount_menu_choice == "3":
                        messages_menu_choice = social_network_ui.messagesMenu()
                        while True:
                            #Sending messages
                            if messages_menu_choice == "1":
                                if len(p1.friendList) == 0:
                                    print("You can only send messages to friends. Please add a friend and try again.")
                                else:
                                    print("You can send a message to any of your friends. Your current friends list is",p1.friendList)
                                    recipient = input("Who would you like to send a message to? ")
                                    sender = p1.username

                                    if recipient not in p1.friendList:
                                        print("The recipient you entered is not in your friend list")
                                    else:
                                        message = input("What would you like to send your friend? ")
                                        p2 = ai_social_network.listPeople[ai_social_network.listUsernames.index(recipient)]
                                        p2.inbox.append(f"{sender} says: {message}")
                                        print(p2.inbox)
                                        print("Your message to",recipient,"has been sent")

                                break

                            #Viewing inbox
                            elif messages_menu_choice == "2":
                                if len(p1.inbox) == 0:
                                    print("\nYou have not recieved any messages")
                                else:
                                    print("\nYour current messages are:",p1.inbox)
                                break
                            
                            #Going back
                            elif messages_menu_choice == "3":
                                break

                            else:
                                print("Your input is invalid. Try Again!")

                        messages_menu_choice = social_network_ui.messagesMenu()


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



        
