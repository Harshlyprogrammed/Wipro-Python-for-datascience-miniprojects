#Write a program to print the sum of all the digits of a given number.

num = int (input("write the number: "))
digit_sum = 0
while(num>0):

    digit=num%10

    digit_sum +=digit

    num = num//10

print(digit_sum)

