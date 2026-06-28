#Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.

num1 = int(input("number 1 : "))
num2 = int(input("number 2 : "))

if (num1%10 == num2%10):
    print("true")
else:
    print("flase")