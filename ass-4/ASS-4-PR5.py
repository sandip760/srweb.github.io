def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

a=int(input("Enter a no :- "))
b=int(input("Enter a no :- "))
c=int(input("Enter a no :- "))

x=largest(a,b,c)
print("Largest no is ",x)
