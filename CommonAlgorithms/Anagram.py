
def anagram(str1, str2):
    if len(str1) != len(str2):
        return 0
    else:
        temp = ""
        if temp.join(sorted(str1.lower())) == temp.join(sorted(str2.lower())):
            return 1
        else:
            return 0


result = anagram("Akhil", "AKHILpop")

if result:
    print("It is anagram")
else:
    print("Not an anagram")
