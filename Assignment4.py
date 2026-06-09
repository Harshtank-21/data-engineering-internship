# Assignment 4
import math

def max_of_three(a,b,c): return max(a,b,c)
def distinct(lst): return list(set(lst))
def multiply(lst):
    result=1
    for i in lst: result*=i
    return result
def factorial(n): return math.factorial(n)
def reverse_string(s): return s[::-1]
def in_range(n,start,end): return start<=n<=end
def even_numbers(lst): return [i for i in lst if i%2==0]
def is_prime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True
def count_case(s):
    return sum(c.isupper() for c in s), sum(c.islower() for c in s)

with open("sample.txt","w") as f: f.write("Hello")
with open("sample.txt","a") as f: f.write("\nAppended")
with open("sample.txt","r") as f: print(f.read())
