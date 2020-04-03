def URLify(str):
    temp = ""
    for c in str:
        if c in str:
            if c == " ":
                temp += "%20"
            else:
                temp += c
    return temp


print(URLify("My name is Akhil"))