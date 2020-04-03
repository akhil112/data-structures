# Description = Check if string has unique characters

def unique(val):
    return len(val) == len(set(val))


if unique("akhil"):
    print("Unique")
else:
    print("Not unique")
