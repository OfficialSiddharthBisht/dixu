a=int(input("marks of student a out of 100"))
b=int(input("marks of student b out of 100"))
c=int(input("marks of student c out of 100"))
d=int(input("marks of student d out of 100"))
# average=sum of observations/total number of observations
print(int((a+b+c+d)/4))

if(a<=b and a<= c and a <= d):
    print("Minimum ",a)
elif(b<=a and b<=c and b<=d):
    print("minimum ",b)
elif(c<=a and c<=b and c<=d):
    print("minimum ",c)
elif(d<=a and d<=b and d<=c):
    print("minimum ",d)

if(a<33):
    print("a fail")
if(b<33):
    print("b fail")
if(c<33):
    print("c fail")
if(d<33):
    print("d fail")

a*=0.95
b*=0.95
c*=0.95
d=int(d*0.95)
print(a,b,c,d)
