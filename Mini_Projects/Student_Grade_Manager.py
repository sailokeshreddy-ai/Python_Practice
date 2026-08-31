#Student Grade Manager
name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")

maths = int(input("Enter your Maths marks: "))
python = int(input("Enter your Python marks: "))
english = int(input("Enter your English marks: "))

total = maths + python + english

percentage = (total / 300) * 100
