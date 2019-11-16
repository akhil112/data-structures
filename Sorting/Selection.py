a = [-3, 4, 1, 88, 4]

for i in range(0,len(a),1):
    small = i
    for j in range(i+1,len(a)):
        if a[j] < a[small]:
            small = a[j]
            a[j], a[small] = a[small], a[j]


print(a)



