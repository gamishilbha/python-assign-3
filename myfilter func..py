"""
Python Assignment 2-Gami Shilbha
myfilter function - even numbers
"""

def myfilter(x):
    a=[]
    for i in range(x+1):
        if i%2==0:
            a.insert(len(a), i)
    print(*a)
       
myfilter(20)
