#Tip_calculator - it helps you calculate the amount of tip each member should pay, based on the bill
print("welcome to tip calculator")
bill_amount = float(input("What is your bill amount?: "))
tip_percentage = float(input("How much tip would you like to pay?: "))
split_pax = int(input("How much people to split the bill with: "))

tip_pp = round(((bill_amount * (tip_percentage/100)) + bill_amount)/split_pax,2)
print(f"Your entire bill amount was {bill_amount}, based on {tip_percentage} tip percentage, everyone should pay {tip_pp}")