#checking odd or even

num = int(input("Enter a number: "))

rem = num % 2

if(rem == 0):
    print("EVEN")
else:
    print("ODD")

#other method to check odd or even
num1 = int(input("Enter a number: "))
if(num1 % 2 == 0):
    print("EVEN")
else:
    print("ODD")