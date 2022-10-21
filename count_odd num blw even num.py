n=int(input())
m=list(map(int,input().strip().split()))[:n]
a=1
b=1
c=1
d=0
for i in range(len(m)):
    a=b
    b=c
    c=m[i]
    if a%2==0 and c%2==0:
        if b%2:
            d+=1
print(d)
