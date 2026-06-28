#Write a program to reverse a given number and print.

num =int(input("write the number : "))

reverse = ""

while num>0:
    digit = num%10

    reverse += str(digit)

    num //=10
print(reverse)
