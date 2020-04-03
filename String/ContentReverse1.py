# Write a Program To REVERSE internal content of every
#  second word present in the given string


# Write a Program To REVERSE internal content of each word?

def reverse(content):
    temp = []
    words = content.split(" ")
    for word in words:
        if words.index(word) % 2 == 0:
            temp.append(word)
        else:
            temp.append("".join(list(word)[::-1]))
    return " ".join(temp)





print(reverse("I am going to russia"))