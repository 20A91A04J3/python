def add(a,b):
   print("addition of {},{}={}".format(a,b,a+b))
def sub(a,b):
   print("subtraction of {},{}={}".format(a,b,a-b))
def multi(a,b):
   print("multiplication of {},{}={}".format(a,b,a*b))
def div(a,b):
   print("division of {},{}={}".format(a,b,a/b))
a=int(input("enter a number"))
b=int(input("enter a value"))
c=input("enter an operator")
if c=='+':
    add(a,b)
elif c=='-':
    sub(a,b)
elif c=='*':
    multi(a,b)
else:
    div(a,b)
