# Python program to create set difference and symmetric difference

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print("Set 1:", s1)
print("Set 2:", s2)
difference_set = s1.difference(s2)
print("Difference (Set1 - Set2):", difference_set)

symmetric_diff_set = s1.symmetric_difference(s2)
print("Symmetric Difference:", symmetric_diff_set)
