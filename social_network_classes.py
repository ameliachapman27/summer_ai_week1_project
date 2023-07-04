# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.listPeople = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        self.listUsernames = []
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        #implement function that creates account here
        print("Creating ...")
        username = input("Enter a username: ")
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        favColor = input("Enter your favorite color: ")
        favAnimal = input("Enter your favorite animal: ")
        p1 = Person(username,name,age,favColor,favAnimal)
        p2 = Person(username,name,age,favColor,favAnimal)
        print(f"Your name is {p1.name} and your age is {p1.age}. Your favorite color is {p1.favColor} and your favorite animal is a {p1.favAnimal}. Write down your username, {p1.username}, so you can log back in later.")
        self.listPeople.append(p1)
        self.listUsernames.append(p1.username)



class Person:
    def __init__(self, username, name, age, favColor, favAnimal):
        self.username = username
        self.name = name
        self.age = age
        self.favColor = favColor
        self.favAnimal = favAnimal
        self.friendList = []
        self.inbox = []

    def add_friend(self, person_object):
        person_object = input("Enter the name of a friend to add: ")
        self.friendlist.append(person_object)

    def send_message(self):
        #implement sending message to friend here
        pass