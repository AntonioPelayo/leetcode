/* Antonio Pelayo April 4, 2020
Problem: 283 Move Zeros
Difficulty: Easy

Given an array nums, write a function to move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
*/

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        
        // Count how many Zeros
        int numZeros = 0;
        for (int i = 0; i < n; i++)
            if (nums[i] == 0)
                numZeros++;
        
        // Create vector with non-zero elements
        vector<int> ans;
        
        for (int i = 0; i < n; i++)
            if (nums[i] != 0)
                ans.push_back(nums[i]);
        
        // Move zeros to end
        for (int i = 0; i < numZeros; i++)
            ans.push_back(0);
       
        // Assign result
        for (int i = 0; i < n; i++)
            nums[i] = ans[i];
    }
};
