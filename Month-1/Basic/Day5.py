#Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.
#using bubble sort
class Solution:
    def kthSmallest(self, arr, k):
        
        n = len(arr)
        
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j] , arr[j+1] =arr[j+1] , arr[j]
        return arr[k-1]
s = Solution()
print(s.kthSmallest([7,10,4,6,12],2))

#manual reversing using 2 pointers
arr = [1,2,3,4,5]
left = 0
right = len(arr)-1
while left<right:
  arr[left] , arr[right] = arr[right] , arr[left]
  left += 1
  right -= 1
print(arr)

#count frequency of elements using dictionary
arr1 = [1,2,2,1,1,3,3,3,3]
count ={}

for x in arr1:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1
print(count)
