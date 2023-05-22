n=int(input("enter the binary no"))

d=0
i=1
while(n!=0):
    r=n%10
    d=d+(i*r)
    i=i*2
    n=n//10

print("the desimal no is",d)
