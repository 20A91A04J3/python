n=int(input("enter the number for which u want to find the factorial"))
s=n
for i in range(n-1,0,-1):
    s=s*i
print('the factorial of {} is:'.format(n),s)    
