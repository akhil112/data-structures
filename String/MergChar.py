# Wrt a prog to merge characters of 2 strings into a single string
# by taking characters altern

def merge(str1,str2):
    temp = ""
    if len(str1) == len(str2):
        for i in range(len(str1)):
            temp = temp+str1[i]
            temp = temp+str2[i]

    else:
        i, j = 0, 0
        while i < len(str1):
            temp = temp+str1[i]
            i += 1


        while j < len(str2):
            temp = temp + str2[j]
            j += 1


    return temp


print(merge("israelkjhjkhj", "rusfgfgfsia"))