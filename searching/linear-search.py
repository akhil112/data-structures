def search(lst,x):
    for i in lst:
        if lst[i] == x:
            return i
        else:
            return -1
            
            
result = search([4,5,6,8,9,3],9)

if result!=-1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in the list ")