a=int(input("enter first number"))
def multiply(a):
    product=1
    for i in range(1,a+1):
        product=product*i
    return(product)

x=multiply(a)
print(x)

