# Assignment 2
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
s = s1 + s2
print(s.lower(), s.upper(), s.title(), s.swapcase())
print(s.capitalize(), s.casefold(), s.center(30))
print(s.count("a"), s.endswith("a"), s.find("a"))
print(s.isalnum(), s.isdigit(), s.isnumeric(), s.isspace())
print(s.replace("a","@"))

a=10
a+=5; a-=2; a*=2; a/=2
print(a)

marks = [float(input(f"Subject {i+1}: ")) for i in range(5)]
percentage = sum(marks)/5
if percentage>=60: grade='A'
elif percentage>=50: grade='B'
elif percentage>=40: grade='C'
elif percentage>=33: grade='D'
else: grade='F'
print("Grade:", grade)
