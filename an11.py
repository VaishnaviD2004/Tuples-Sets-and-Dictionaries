# Python script to check if a given key exists in a dictionary

dict = {1: "Apple", 2: "Banana", 3: "Cherry"}

print("Dictionary:", dict)
key = int(input("Enter a key to check: "))

if key in dict:
    print(f"Key {key} exists in the dictionary with value '{dict[key]}'")
else:
    print(f"Key {key} does not exist in the dictionary")
