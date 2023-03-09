c0 = int(input())
i = 0
if c0 > 0:
    while c0 != 1:
        if c0 % 2 != 0:
            c0 = 3*c0+1
            i = i+1
            print('%d' %c0)
        if c0 % 2 ==0:
            c0=c0/2
            i = i+1
            print('%d' %c0)
    print("step = %d" %i)
