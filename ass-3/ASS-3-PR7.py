n=int(input("enter a no"))

i=1
sum=0
while(n>i):
    if(n%i==0):
        sum=sum+i
    i=i+1

if(sum==n):
    print("the no is perfect no")
else:
    print("the no is not a perfect no")
    
