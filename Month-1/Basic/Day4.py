#Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.
class Solution:
    def search(self, arr, x):
        if x in arr:
            return arr.index(x)
        else:
            return -1
s = Solution()
print(s.search([10,20,30,40,50],30))
print(s.search([6,7,8,9],10))

#Given an array arr[]. The task is to find the largest element and return it.
class Solution:
    def largest(self, arr):
       max = arr[0]
       for i in arr:
           if i>=max:
              max = i
       return max
p = Solution()
print(p.largest([10,7,101,8,56,89]))
    
#You are given an array of integers arr[]. You have to reverse the given array.
class Reverse:
    def rev(self,arr):
        n = len(arr)
        temp = [0]*n
        for i in range(len(arr)):
            temp[i] = arr[n-i-1]
        for i in range(len(arr)):
            arr[i] = temp[i]
        return arr
r = Reverse()
print(r.rev([6,7,8]))
print(r.rev([10,4,7,9]))
