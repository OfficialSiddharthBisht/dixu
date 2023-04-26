def sum(a):
    sum=0
    for i in range(1,a+1):
        sum=sum+i
    return(sum)

a=int(input("enter any number"))
x=sum(a)
print(x)
