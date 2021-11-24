def collatz(num):
    while num != 1:
        print(num, end = ' ')
        if num & 1:
            num = 3 * n + 1
        else:
            num = num // 2
    print(num)
 


 
