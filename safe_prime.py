from math import *
def isprime(num):
    if num==1:
        return False
    sq=int(sqrt(num))
    for i in range(2,sq+1):
        if num%i==0:
            return False
        return True
num=int(input())
if isprime(num):
    print("prime")
    if isprime(num//2):
          print("safe prime")
    else:
        print("not a safe prime")
else:
    print("not a prime")
