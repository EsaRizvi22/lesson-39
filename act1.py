#Write a Python program first to take a number as an input from the user, 
# then check whether that number is even or odd and
#  print the result.

num=int(input("Enter a number"))

if (num%2==0):
    print(num," is even")
else:
    print(num," is odd")