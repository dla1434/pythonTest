for n in range(2, 10):
    for x in range(1, 10):
        print(n, '*', x, '==', n*x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            # break
        else:
            print(n, 'is a prime number')