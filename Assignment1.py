# Assignment 1
print("Hello", "World", sep="-")
print("Python", end=" Programming\n")
name = input("Enter your name: ")
print("Hello,", name)

student = input("Student Name: ")
cls = input("Class: ")
marks = [float(input(f"Subject {i+1}: ")) for i in range(5)]
total = sum(marks)
percentage = total / 5
print(f"Name: {student}\nClass: {cls}\nPercentage: {percentage:.2f}%")
