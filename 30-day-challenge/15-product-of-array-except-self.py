"""Antonio Pelayo April 15, 2020
Problem: 238 Product of Array Except Self
Difficulty: Medium

Given an array nums of n integers where n > 1,  return an array output such that 
output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or 
suffix of the array (including the whole array) fits in a 32 bit integer.

Note: 
Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not 
count as extra space for the purpose of space complexity analysis.)
"""

def productExceptSelf(nums):
    products = []
    product = 1
        
    # Initialize product vector with product of previous elements
    for i in range(len(nums)):
        products.append(product)
        product *= nums[i]

    product = 1
            
    # Compute product with elements after nums[i]
    for i in range(len(nums) - 1, -1, -1):
        products[i] *= product
        product *= nums[i]

    return products

a = [1, 2, 3, 4]

print(productExceptSelf(a))