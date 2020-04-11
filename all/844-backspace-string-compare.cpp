/* Antonio Pelayo April 9, 2020
Problem: 844 Backspace String Compare
Difficulty: Easy

Given two strings S and T, return if they are equal when both are typed into 
empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Follow up:
Can you solve it in O(N) time and O(1) space?
*/

class Solution {
public:
    bool backspaceCompare(string S, string T) {
        vector<char> vS, vT;

        // Get compiled string for S
        for (auto c: S) {
            if (c == '#' and vS.size() > 0) 
                vS.pop_back();
            else if (c != '#') 
                vS.push_back(c);
        }
        
        // Get compiled string for T
        for (auto c: T) {
            if (c == '#' and vT.size() > 0) 
                vT.pop_back();
            else if (c != '#') 
                vT.push_back(c);
        }
    
        return vS == vT;
    }
};
