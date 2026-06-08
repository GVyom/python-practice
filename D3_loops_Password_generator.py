#Pass Word Generator
import random
print("welcom to Password Generator")
letter = int(input("how many letters would you like in your password?:\n"))
symbol = int(input("how many syombols would you like in your password?:\n"))
number = int(input("how many numbers would you like in your password?:\n"))

letters = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=","?","/"]

password = ""
for char in range(0, letter):
    password += random.choice(letters)

for char in range(0, symbol):
    password += random.choice(symbols)

for char in range(0, number):
    password += random.choice(numbers)

print(password)

password_list = []
for char in range(0, letter):
    password_list.append(random.choice(letters))

for char in range(0, symbol):
    password_list.append(random.choice(symbols))

for char in range(0, number):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password1 = ""
for chart in password_list:
    password1 += chart
print(password1)