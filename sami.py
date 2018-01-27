import random
import array
a=input("enter a")
b=input("enter b")
a=int(a)
b=int(b)
c=input("no of times to generate")
c=int(c)
per2=0
per1=0
d=0
d1=0
arr=[]
z=int((a+b)/2)
print(z)
for i in range(1,c+1):
    x=random.randint(a,b)
    x=int(x)
    arr.append(x)
print(arr)
for i in range(0,c):
    if(arr[i]>=z):
        d=d+1
        per1=d/c*100
        if(per1<=73):
            print(arr[i] , i+1)
        else:
            print(arr[i]-z , i+1)
    else:
        d1=d1+1
        per2=d1/c*100
        if(per2<=27):
            print(arr[i] , i+1)
        else:
            print(arr[i]+z , i+1)
