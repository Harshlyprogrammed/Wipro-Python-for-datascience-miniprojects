#Write a program to check if a given number is prime or not.

num = int(input("write the number : "))
is_prime = True

for i in range(2,num):
    if(num%i==0):
        is_prime = False
        break

print(is_prime)