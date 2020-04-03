def remove_duplicate(arr):
    dic = []

    for i in arr:
        if i in dic:
            continue
        else:
            dic.append(i)
    return "".join(dic)

print(remove_duplicate("azzbcdabbcdabbccddeef"))