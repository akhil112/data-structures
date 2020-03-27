def prime(start, end):
    for val in range(start, end+1):
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            print(val)


prime(1, 100)