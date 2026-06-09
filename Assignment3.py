# Assignment 3
d = {"name":"Harsh","age":20}
t = (1,2,3)
s = {1,2,3}
print(d,t,s)

def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b if b!=0 else "Undefined"

a,b = map(float,input("Enter two numbers: ").split())
print(add(a,b), sub(a,b), mul(a,b), div(a,b))

num = input("Enter number: ")
print("Palindrome" if num==num[::-1] else "Not Palindrome")
