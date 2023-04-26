def sum(x,y):
    return(x+y)
def subtract(x,y):
    return(x-y)
def multiply(x,y):
    return(x*y)
def divide(x,y):
    return(x//y)
x=int(input("enter first number"))
y=int(input("enter second number"))
z=input("enter a to add, s to subtract, m to multiply, d to divide")
ans=1
if(z=="a"):
    ans=sum(x,y)
elif(z=="s"):
    ans=subtract(x,y)
elif(z=="m"):
    ans=multiply(x,y)
elif(z=="d"):
    ans=divide(x,y)
print(ans)

    