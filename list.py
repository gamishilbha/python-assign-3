"""
Python assignment 3
Comprehension list
"""

list_a = ['x', 'y', 'z']
   
s_p=[]
def second_look(in_put):
    for i in range(len(in_put)):
        s_p.append(in_put[i])

    for i in range(len(in_put)):
        s_p.append(in_put[i]+in_put[i])

    for i in range(len(in_put)):
        s_p.append(in_put[i]+in_put[i]+in_put[i])
       
    for i in range(len(in_put)):
        s_p.append(in_put[i]+in_put[i]+in_put[i]+in_put[i])
second_look(list_a)
print('The first look of the comprehension list is :\n', s_p)
print('The second look of the comprehension list is :\n', sorted(s_p))


"""
number list
"""
num=[]
a=[[2],[3],[4],[5],[6]]

s=0
        
while s<(len(a)-2):
    for i in range(s, s+3):
        num.append(a[i])
    s+=1

x=2
for j in range(4):
    b=[]
    for i in range(x, x+4):
        b.append(i)
    num.append(b)
    x+=1
print("The first number pattern list is :\n",num)

a=(1,1)
num1=[]
num1.append(a)
for i in range(2):
    b=list(a)
    b[0]=a[0]+1
    a=tuple(b)
    num1.append(a)
c=(1,2)  
num1.append(c)
for i in range(2):
    d=list(c)
    d[0]=c[0]+1
    c=tuple(d)
    num1.append(c)   
e=(1,3)  
num1.append(e)
for i in range(2):
    f=list(e)
    f[0]=e[0]+1
    e=tuple(f)
    num1.append(e)          
     
print("The last pattern in the Comprehension list is :\n", num1)
