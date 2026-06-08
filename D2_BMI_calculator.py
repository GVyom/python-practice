print("This application can help you calculate your boday mass index")
W = input("please enter your weight in Kgs:")
H = input("please enter your height in meters")
weight = int(W)
hieght = float(H)
BMI = weight/hieght**2

if BMI < 18.5:
    print(f"your BMI is {round(BMI,2)}, and you are underweight")
elif BMI < 25:
    print(f"your BMI is {round(BMI,2)}, and you are normal")
else:
    print(f"your BMI is {round(BMI,2)}, and you ar overweight")
    