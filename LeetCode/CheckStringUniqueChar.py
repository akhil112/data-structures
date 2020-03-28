# Description = Check if string has unique characters

def unique(val):
    if len(val) == len(set([c for c in val])):
        return 1
    return 0



if unique("putinnnnn"):
    print("Unique")
else:
    print("Not unique")
