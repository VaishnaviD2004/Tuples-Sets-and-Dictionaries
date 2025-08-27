# Program to check if an element exists in a tuple
t = (10, 20, 30, 40, 50)

element = int(input("Enter the element to check: "))

# Check existence
if element in t:
    print(f"Yes, {element} exists in the tuple.")
else:
    print(f"No, {element} does not exist in the tuple.")
