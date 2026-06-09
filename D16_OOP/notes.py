#OOP: Object Oriented Programming -> helped us to move from procedural programming to more advanced functionality
#Larger project into smaller pieces -> worked on by different teams -> reuseable as and when needed
#OOP Allows to develop specialised functions
## -> What it has? || Attributed or variables specific to one objects i.e. waiter1
## -> What it does? || Methods or functions specific to one objects i.e. waiter2
#Trying to model real life objects -> now waiter is a class, and waiter1 or waiter2 is Object
#Simpler terms -> Class is defined Attributes and Methods, used to make single or multiple objects

#car = CarBlueprint() #car = object, and CarBlueprint() = Class

import turtle #Blueprint already created by someone
from turtle import Turtle, Screen
timmy = Turtle() #Fetching Turtle (class) from turtle
print(timmy)
timmy.shape("turtle")
timmy.color("green")
turtle.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()