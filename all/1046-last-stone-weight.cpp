/* Antonio Pelayo April 12, 2020
Problem: 1046 Last Stone Weight
Difficulty: Easy

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose 
the stones have weights x and y with x <= y.  The result of this smash is:
  * If x == y, both stones are totally destroyed;
  * If x != y, the stone of weight x is totally destroyed, and the stone of 
    weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 
0 if there are no stones left.)

Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

Note:
1 <= stones.length <= 30
1 <= stones[i] <= 1000
*/

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        // Can we return a value yet? 
        if (stones.size() == 0) return 0;
        else if (stones.size() == 1) return stones[0];
        
        int heaviestIndex = 0;
        int heaviestValue = stones[heaviestIndex];
        int nextHeaviestIndex = 1;
        int nextHeaviestValue = stones[nextHeaviestIndex];

        // Grab 2 heaviest stones
        for (int i = 0; i < stones.size(); i++) {
            if (stones[i] >= heaviestValue and i != heaviestIndex) {
                nextHeaviestValue = heaviestValue;
                nextHeaviestIndex = heaviestIndex;
                heaviestValue = stones[i];
                heaviestIndex = i;
            }
            else if (stones[i] >= nextHeaviestValue and 
                     i != nextHeaviestIndex and 
                     i != heaviestIndex) {
                nextHeaviestIndex = i;
                nextHeaviestValue = stones[i];
            }
        }
        
        // 'Smash' stones together
        if (heaviestValue == nextHeaviestValue) {
            // Both are destroyed
            stones[heaviestIndex] = stones[stones.size()-1];
            stones.pop_back();
            stones[nextHeaviestIndex] = stones[stones.size()-1];
            stones.pop_back();
        } else {
            // Smaller stone destroyed heaviest weight recalculated
            stones[heaviestIndex] -= stones[nextHeaviestIndex];
            stones[nextHeaviestIndex] = stones[stones.size()-1];
            stones.pop_back();
        }
             
        // Recurse
        return lastStoneWeight(stones);
    }
};
