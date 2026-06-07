#Day - 8 def with input || Cipher
def greet():
    print("hi")
    print("hi")
    print("hi")

def greet_with_name(name): #here name is a changeable variable, while function when we call it in () is the input
     print(f"hi {name}")

#functions with multiple input
def greet_with(name, location):
     print(f"Hi my name is {name} and my location is {location}")

#greet_with(location="jalandhar", name="vyom")

#positional argument - order of argument will always match the order for paramater
#unless key-word argument like above is given

#Caesar Cipher
print('''   _______                                _______  _       _               
  (  ____ \|\     /||\     /||\     /|    (  ____ \| \    /\\__   __/|\     /|
  | (    \/| )   ( || )   ( || )   ( |    | (    \/|  \  / /   ) (   | )   ( |
  | |      | (___) || (___) || (___) |    | |      |  (_/ /    | |   | (___) |
  | |      |  ___  ||  ___  ||  ___  |    | |      |   _ (     | |   |  ___  |
  | |      | (   ) || (   ) || (   ) |    | |      |  ( \ \    | |   | (   ) |
  | (____/\| )   ( || )   ( || )   ( |    | (____/\|  /  \ \___) (___| )   ( |
  (_______/|/     \||/     \||/     \|    (_______/|_/    \/\_______/|/     \|''')

direction = input("type \'encode\' to encrypt, type \'decode\' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
     cipher_text = ""
     for i in original_text:
          shifted_position = alphabet.index(i) + shift_amount
          shifted_position %= len(alphabet)
          cipher_text += alphabet[shifted_position]
     print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
     cipher_text = ""
     for i in original_text:
          shifted_position = alphabet.index(i) - shift_amount
          shifted_position %= len(alphabet)
          cipher_text += alphabet[shifted_position]
     print(f"Here is the encoded result: {cipher_text}")

if direction == "encode":
     encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
     decrypt(original_text=text, shift_amount=shift)
else:
     print("Please type valid input")

#OR ***************************************************************************************
def caesar(original_text, shift_amount, e_or_d):
     cipher_text = ""
     if e_or_d == "decode":
          shift_amount *= -1
     for i in original_text:
          if i not in alphabet:
               cipher_text += i
          else:
               shifted_position = alphabet.index(i) + shift_amount
               shifted_position %= len(alphabet)
               cipher_text += alphabet[shifted_position]
     print(f"Here is the encoded result: {cipher_text}")

should_continue = True
while should_continue:
     print('''   _______                                _______  _       _               
  (  ____ \|\     /||\     /||\     /|    (  ____ \| \    /\\__   __/|\     /|
  | (    \/| )   ( || )   ( || )   ( |    | (    \/|  \  / /   ) (   | )   ( |
  | |      | (___) || (___) || (___) |    | |      |  (_/ /    | |   | (___) |
  | |      |  ___  ||  ___  ||  ___  |    | |      |   _ (     | |   |  ___  |
  | |      | (   ) || (   ) || (   ) |    | |      |  ( \ \    | |   | (   ) |
  | (____/\| )   ( || )   ( || )   ( |    | (____/\|  /  \ \___) (___| )   ( |
  (_______/|/     \||/     \||/     \|    (_______/|_/    \/\_______/|/     \|''')

     direction = input("type \'encode\' to encrypt, type \'decode\' to decrypt: ").lower()
     text = input("Type your message: ").lower()
     shift = int(input("Type the shift number: "))
     caesar(original_text=text, shift_amount=shift, e_or_d=direction)
     restart = input("continue? Yes or no: ").lower()
     if restart == "no":
          should_continue = False
          print("goodbye")