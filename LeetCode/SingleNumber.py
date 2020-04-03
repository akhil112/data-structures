
def single_number(arr):
    dic = {}

    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for key,val in dic.items():
        if val == 1:
            return key


print(single_number([1, 2, 2, 3, 1]))