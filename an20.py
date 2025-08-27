# Program to create a shallow copy of a set

o_set = {1, 2, 3, 4, 5}

copied_set = o_set.copy()

print("Original Set:", o_set)
print("Shallow Copy:", copied_set)

print(" Are both sets the same object?", o_set is copied_set)
