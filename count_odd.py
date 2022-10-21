n=int(input())
m=list(map(int,input().strip().split()))[:n]
a=0
b=0
c=0
d=0
for i in range(len(m)):
    a=b
    b=c
    c=m[i]
    if a%2 and c%2:
        if b%2:
            d+=1
print(d)
