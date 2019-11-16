string  = "I am going to russia russia"


dict = {}



for i in string.split():
    if i in dict:
        val = dict[i]
        dict[i] += 1

    else:
        dict[i] = 1

print(dict)