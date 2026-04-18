#How THIS WORKS?
#This is typical If/Else functionality
#Case: Check for eligibility of a person for the ride
#Conditions - Anyone above 120 cm can go, child (<=12 =5), Youth (between 12-18 = 7), Adults (10) for normal ride tickets, but if they want photos that will be additional $3
Height = int(input("what is your height: ")) #for first check - height
Bill = 0 #Dummy assigned value for variable creation, and it will varies depending on inputs
if Height >= 120:
    Age = int(input("what is your age?: ")) #second input pops up for price check, only after confirming 120 >=
    if Age <= 12:
        Bill = 5 #Price re-assigned by code automatically to 5 as age is <= 12 - run 1
        print("Child tickets are $5")
    elif Age <= 18:
        Bill = 7 #Price re-assigning - run 1
        print("Youth tickets are $7.")
    else:
        Bill = 10 #price re-assigning - run 1
        print("Adult tickets $10.")

    wants_picture = input("Do you want to take picture for your memories? (yes/no): " )
    if wants_picture == "yes":
        Bill += 3 #Price re-assigning run2, if wants_picture = "yes"
        
    print(f"your final bill is {Bill}")
else:
    print("Sorry you are not eligible for the ride.")