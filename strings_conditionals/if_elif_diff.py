#if condition is true then it will execute the block of code under if statement. If the condition is false then it will check the elif condition and if that is true then it will execute the block of code under elif statement. If both conditions are false then it will execute the block of code under else statement.
#it won't check the elif condition if the if condition is true. It will only check the elif condition if the if condition is false.

num = 3

if(num > 1):
    print("The number is greater than 1")
elif(num > 2): # This condition is not checked because the if condition is true
    print("The number is greater than 2")

num1 = 3
if(num1 > 1):
    print("The number is greater than 1")
if(num1 > 2): # This condition is checked because the if condition is true
    print("The number is greater than 2")
else:
    print("The number is not greater than 2")