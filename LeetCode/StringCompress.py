
def compress(val):
    dic = {}
    for i in val:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    temp = ""
    for key, val in dic.items():
        temp += key
        temp += str(val)
    return temp



print(compress("aabbbccccddddd"))