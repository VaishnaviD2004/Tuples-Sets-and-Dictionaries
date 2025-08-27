# Program to find repeated items in a tuple

tuple = (1, 3, 5, 2, 3, 7, 1, 9, 5, 2, 5)

repeated_items = []
for item in tuple:
    if tuple.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)

print("Original Tuple:", tuple)
print("Repeated Items:", repeated_items)
