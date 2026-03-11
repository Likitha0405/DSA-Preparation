#alternates in an array:
'''arr = [10,20,30,40,50]
for i in range(len(arr)):
    if i % 2 == 0:
        print(arr[i])

arr2 = [1,2,3,4,5]
for i in range(0,len(arr2),2):
    print(arr2[i])
'''
class solution:
    def alternates(self,arr):
        for i in range(0,len(arr),2):
            print(arr[i])
s = solution()
s.alternates([1,2,3,4,5])
s.alternates([10,20,30])