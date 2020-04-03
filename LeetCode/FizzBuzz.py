def fizzbuzz(values):
    for i in values:
        if (i%3) == 0 and   (i%5) == 0:
            print("FizzBuzz")
        elif (i%3)==0:
            print("Fizz")
        elif (i%5) == 0:
            print("buzz")
        else:
            print(i)




fizzbuzz([3, 5, 15])
