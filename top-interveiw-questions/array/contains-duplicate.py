''' Antonio Pelayo March 15, 2020
Problem: Contains Duplicate
Difficulty: Easy

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the 
array, and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

def containsDuplicate(nums):
  # Edge cases
  if len(nums) < 2:
    return False

  nums = sorted(nums)
  
  # Numbers will be next to eachother if duplicate
  for i in range(len(nums) - 1):
    if nums[i] == nums[i+1]:
      return True
  
  # No duplicates found
  return False

a = [1, 2, 3, 1]
b = [1, 2, 3, 4]
c = [1, 1, 1, 3, 3, 5, 3, 2, 4, 2]

print(containsDuplicate(a))
print(containsDuplicate(b))
print(containsDuplicate(c))

