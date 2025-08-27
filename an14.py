# Python program to create a list of tuples (number, square)
n = int(input("Enter the range (e.g., 5 for 1 to 5): "))
result = [(x, x**2) for x in range(1, n+1)]

print("List of tuples (number, square):")
print(result)
