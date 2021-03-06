''' Antonio Pelayo April 2, 2020
Problem: 189 Rotate Array
Difficulty: Easy

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:
Try to come up as many solutions as you can, there are at least 3 different ways 
to solve this problem.

Could you do it in-place with O(1) extra space?
'''

def rotate(nums, k):
    # Array with same length as nums
    rotated = [0 for i in range(len(nums))]

    # Set numbers in rotated array
    for i in range(len(nums)):
        rotated[(i + k) % len(nums)] = nums[i]

    # Assign numbers back to nums array
    for i in range(len(nums)):
        nums[i] = rotated[i]

    return nums


a = {'nums': [1, 2, 3, 4, 5, 6, 7],
     'k': 3}
b = {'nums': [-1, -100, 3, 99],
     'k': 2}

print(f"{a['nums']} rotated {a['k']} times is {rotate(a['nums'], a['k'])}")
print(f"{b['nums']} rotated {b['k']} times is {rotate(b['nums'], b['k'])}")