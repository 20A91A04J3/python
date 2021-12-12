n=int(input())
flag=0
for i in range(2,n):
   if n==1:
       print("not a prime or composite")
   elif n%i==0:
         flag=1
         break
if flag!=0:
   print("not a prime")
else:
   print("prime")
