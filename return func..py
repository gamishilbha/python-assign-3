"""
Python Assignment 2-Gami Shilbha
myreduce function 
"""
def sum(x1, x2): 
    return x1 + x2

def my_reduce(func, seq):
     first = seq[0]
     for i in seq[1:]:
        first = sum(first, i)
     return first
 

print("The sum of all the numbers in the given sequence is ", my_reduce(sum, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
