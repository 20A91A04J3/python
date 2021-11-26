a=1
b=4
for row in range(0,5):
    for col in range(0,5):
        if row==0 or row==4:
            print("*",end=' ')
        elif row==a and col==b:
            print('*',end='  ')
            a=a+1
            b=b-1
        else:
            print(end="   ")
    print()
