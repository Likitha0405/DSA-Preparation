#searching
#1. Linear Search
arr = [10, 20, 30, 40]
target = 30

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Not found")

#2. Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1
arr = [2, 5, 8, 12, 16, 23, 38]
target = 16

result = binary_search(arr, target)
print(result)