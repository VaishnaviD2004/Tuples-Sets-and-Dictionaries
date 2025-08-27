# Python script to sort a dictionary by value

dict = {1: 45, 2: 11, 3: 89, 4: 32, 5: 67}

print("Original Dictionary:", dict)

# (ascending)
asc_dict = dict(sorted(dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by value (Ascending):", asc_dict)

#(descending)
desc_dict = dict(sorted(dict.items(), key=lambda item: item[1], reverse=True))
print("Dictionary sorted by value (Descending):", desc_dict)
