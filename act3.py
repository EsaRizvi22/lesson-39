#Write a Python program to check whether a number entered by the user is greater than 50 or not.
#  Also, if it is greater than 50, then check whether it is odd or even.

num=int(input("Enter a number"))

if num>50:
    print("Greater then 50")
    if (num%2==0):
        print("And the number is even")
    else:
        print("And the number is odd")
else:
    print(num," is less then 50")