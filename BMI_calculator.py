print("This application can help you calculate your boday mass index")
W = input("please enter your weight in Kgs:")
H = input("please enter your height in meters")
weight = int(W)
hieght = float(H)
BMI = weight/hieght**2
print(round(BMI,2))
      