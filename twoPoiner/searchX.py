arr=[1,2,3,4,5]
x=2
n=len(arr)
def func(arr,n,x):
    i=0
    str=""
    while(i<n):
        if arr[i]==x:
            return True
        i=i+1
# ans=func(arr,n,x)
# print(ans)
def fun1(arr,n,x):
    for i in range(0,n+1):
        if arr[i]==x:
            return True
# ans=func(arr,n,x)
# print(ans)
def fun2(arr,n,x):
    i=0
    j=n-1
    while(i==j):
        if(arr[i]==x or arr[j]==x):
            return True
        i=i+1
        j=j-1
    return True
# ans=fun2(arr,n,x)
# print(ans)
def fun3(arr,n,x):
    i=0
    j=n-1
    for i in range(0,n):
        if(arr[i] == x or arr[j] == x):
            return True
        j= j-1
    return False
ans=fun3(arr,n,x)
print(ans)
    
            




