#count occurences using linear search
def count_occ(arr, target):
    count = 0
    for x in arr:
        if x == target:
            count += 1
    return count
arr = [1,2,2,3,4,3]
target = 3
print(count_occ(arr,target))

#count occurences using Binary search
def first_occ(arr, target):
    left = 0
    right = len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            ans = mid          
            right = mid - 1    

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return ans


def last_occ(arr, target):
    left = 0
    right = len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            ans = mid          
            left = mid + 1     

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return ans


def count_occ(arr, target):
    first = first_occ(arr, target)

    if first == -1:
        return 0   # element not present

    last = last_occ(arr, target)

    return last - first + 1


# test
arr = [1,2,2,2,3,4]
print(count_occ(arr, 2))