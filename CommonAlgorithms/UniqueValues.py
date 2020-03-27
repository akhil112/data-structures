# Get unique values from a list

def unique(lst):
    temp = []
    for i in lst:
        if i not in temp:
            temp.append(i)
        else:
            continue
    return temp


results = unique([3, 4, 5, 34, 3, 3, 3, 5, 6, 7])

print(results)