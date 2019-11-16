a = [55, -2, 34, 10, 0, 2, -5, 12]

for i in range(1, len(a)):
    for j in range(i-1, -1, -1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
        else:
            break

print(a)















