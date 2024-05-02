print("Enter number of elements: ")
n = int(input())

v = []
print("\nEnter values: ")
for i in range(n):
    x = int(input("Element {}: ".format(i + 1)))
    v.append(x)

print("\nThe array you entered is:", v)

print("\nPerforming Selection Sort on the given array")
for i in range(n):
    z = i
    for j in range(i + 1, n):
        if v[j] < v[z]:
            z = j
    v[i], v[z] = v[z], v[i]

print("\nThe sorted array is:", v)
