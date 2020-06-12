# Write a Program To REVERSE internal content of each word?

def reverse(content):
    temp = []
    for i in content.split(" "):
        temp.append("".join(list(i)[::-1]))
    return " ".join(temp)





print(reverse("I am going to russia"))






