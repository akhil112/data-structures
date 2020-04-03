def list_diff(list1, list2):
	return (list(set(list1) - set(list2)))

# Test Input
list1 = [11, 16, 21, 26, 31, 36, 41]
list2 = [26, 41, 36]

# Run Test
print(list_diff(list1, list2))