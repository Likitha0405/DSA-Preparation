def first_occ(arr, target):
    left = 0
    right = len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            ans = mid          #this stores the answer
            right = mid - 1    #moves left

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return ans
res = first_occ([1,1,2,2,2,3,4],2)
if res != -1:
    print("The first occurence of element found at index",res)
else:
    print("element not found")