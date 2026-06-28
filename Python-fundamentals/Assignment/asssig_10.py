#Write a program to find if the given number is palindrome or not

num =int(input("write the number : "))
orignal = num
reverse = 0
while num>0:
    digit = num%10

    reverse = reverse*10 + digit

    num //=10
if(orignal==reverse):
    print("yes pelindrome")
else:
    print("not pelindrome")
