for i in range(8):
    x = 63 ^ 1<<i
    print(bin(x)[2:],x,1 << i)