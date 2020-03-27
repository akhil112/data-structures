val  = 100

if val > 1:
    for i in range(2, val//2):
        if (val % i) == 0:
            print("Its is not a prime")
            break
    else:
        print("It is a prime")