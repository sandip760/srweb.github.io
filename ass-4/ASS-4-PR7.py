from datetime import *
import calendar
x=datetime.now()
print(x)

y=x.strftime("%d-%b-%y")
print(y)

z=x.strftime("%a-%d-%B-%Y")
print(z)

yy=int(input("enter the year :- "))
mm=int(input("enter the month :-"))

print(calendar.month(yy,mm))

