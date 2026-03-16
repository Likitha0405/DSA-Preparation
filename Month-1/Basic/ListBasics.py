 #max in an array
nums = [3,8,1,10,5]
max = nums[0]
for num in nums:
    if num >= max:
      max = num
print(max)

# min in an array
nums = [3,8,1,10,5]
min = nums[0]
for num in nums:
    if num <= min:
      min = num
print(min)

# count even numbers in an array
nums = [3,8,1,10,5]
count_even = 0
for num in nums:
  if num%2 == 0:
    count_even += 1
print(count_even)

#manual reversing using 2 pointers
arr = [1,2,3,4,5]
left = 0
right = len(arr)-1
while left<right:
  arr[left] , arr[right] = arr[right] , arr[left]
  left += 1
  right -= 1
print(arr)