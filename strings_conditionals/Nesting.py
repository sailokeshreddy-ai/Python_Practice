#Nesting of if else statements
age = int(input("Enter your age: "))

if(age >= 18):
    if(age >= 65):
        print("You are not eligible for driving.")
    else:
        print("You are eligible for driving.")
else:
    print("You are not eligible for driving.")