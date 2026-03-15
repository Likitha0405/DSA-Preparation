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