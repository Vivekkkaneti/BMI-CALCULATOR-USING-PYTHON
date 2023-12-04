Name = input("Enter your name:")
weight = int(input("Enter your weight in pounds:"))
height = int(input("Enter your height in inches"))
BMI = (weight*703)/(height*height)
print(BMI)
if BMI>0:
    if(BMI<18.5):
        print(Name+" "+"You are Underweight")
    elif(BMI<=24.9):
        print(Name+" "+"You are Normal weight")
    elif(BMI<=29.9):
        print(Name+" "+"you are overweight")
    elif(BMI<=34.9):
        print(Name+" "+"You are obese")
    elif(BMI<=39.9):
        print(Name+" "+"You are severe obese")
    else:
        print(Name+" "+"You are Mobidly obese")
else:
    print("Enter Valid Input")