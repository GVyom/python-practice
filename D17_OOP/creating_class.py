#class = Blueprint for creating eventual object
class User: #similar to function but no () || Name of class always Capital
    #pass #passing the class as empty 
    pass

class User1:
    def __init__(self, user_id, username): #init function is called every time we create a new object for this class
        #print("new user being created....") #every time we create a new user using class User() this statement will be printed
        self.id = user_id
        self.username = username
        self.followers = 0 #provided default value, now no need to pass follower count always
        self.following = 0
    
    def follow(self, user1): #self is always a first parameter
        user1.followers += 1
        self.following += 1

user_1 = User()
user_1.id = "001"
user_1.username = "vyom" #attribute creation i.e username is an attribute or simply variable associated with object user_1

#If we have a lot of users, then creating so many variables/attribution will be difficult
#Therefore, we will use Constructor OR initalizing a project
#The above is done by using special function i.e. __init__ function
#i.e. def __init__ (self): --> Line 3 to understand

user_2 = User1("002", "Goyal")
user_3 = User1("003", "Dron")

#Due to class, and attributes created in that class our code time reudced as we do not have to create those attributes for all the Objects we will create
#i.e. now for user3 - I can just pass on the information and do print(user3.id) results will be their id 003


#We can also set any attribute's default value as well

#Creating Methods
#--> Attributes = Variables -> thing an object have
#--> Methods = functions -> thing an object does
#How to create it? -> Well a function in a class
#How to call that function? -> object.function name i.e. my_car.enter_race_mode()
user_2.follow(user_3)
print(user_2.followers)
print(user_2.following)
print(user_3.following)
print(user_3.followers)
