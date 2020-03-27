def unique(store):
    temp = []
    for value in store.values():
        if value not in temp:
            temp.append(value)
        else:
            continue
    return temp


store = {'Name': 'Akhil', 'Age': 22, 'Country': "putin", "Name1": "Akhil"}

print(unique(store))