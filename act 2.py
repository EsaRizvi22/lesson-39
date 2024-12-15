#Write a Python program that takes height and weight as an input from the user, 
# calculates BMI and, based on the value of BMI, 
# displays the resultant category in which the user falls.


height=int(input("Enter your height"))
weight=int(input("Enter your weight"))

bmi=weight/(height/100)**2

if bmi<=18.4:
    print("you are underweight",bmi)
elif bmi<=24.9:
    print("you are healthy",bmi)
elif bmi<=29.9:
    print("You are overweight",bmi)
elif bmi<=34.9:
    print("You are severly overweight",bmi)
elif bmi<=39.9:
    print("You are obese",bmi)
else:
    print("You are Severly overweight",bmi)