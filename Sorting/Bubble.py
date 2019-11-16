lst = [3, 4, 5, 3, 1, 99, 0, 7]
n = len(lst)
for i in range(n):
    for i in range(0,n-i-1):
        if lst[i] > lst[i+1]:
            temp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = temp
print(lst)


