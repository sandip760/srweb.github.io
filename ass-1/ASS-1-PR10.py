s=int(input("enter the second"))
print(s,"second is",end=" ")
print(s//3600,"hours ",end="")
s=s%3600
print(s//60,"minutes ",end="")
s=s%60
print(s,"second ")
