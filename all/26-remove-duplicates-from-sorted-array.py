''' Antonio Pelayo Mar 1, 2020
Problem: 26 Remove Duplicates from Sorted Array
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.'''

def removeDuplicates(nums):
  if not nums:
    return 0

  i = 1    # Start at 2nd place, 1st isnt a dupe of 1st 

  while i < len(nums):
    if nums[i] == nums[i-1]:
      nums.pop(i)    # Remove
    else:
      i += 1

  return len(nums)

a = [1,1,2]
b = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(a))
print(removeDuplicates(b))
