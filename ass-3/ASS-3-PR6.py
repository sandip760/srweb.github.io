n=int(input("enter a  no"))

s=n
rev=0
while(n!=0):
    r=n%10
    rev=rev*10+r
    n=n//10

if(rev==s):
    print("the no is palindrome no")
else:
    print("the no is not a palindrome no")
