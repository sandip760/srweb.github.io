x=int(input("enter a no"))
c=0
if x==1 :
    print("no is not a prime no")
elif x>1:
    for i in range(2,x):
        if(x%i==0):
            c=1
            break

if(c==0):
    print("no is prime no")
else:
    print("no is not a prime no")
    
