n=int(input("enter a no"))
sum=0

while(n!=0):
    sum=sum+n%10
    n=n//10

print("sum of the digit of the no is:-",sum)
