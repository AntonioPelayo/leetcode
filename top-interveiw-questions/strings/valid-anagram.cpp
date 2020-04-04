/* Antonio Pelayo April 3, 2020
Problem: 242 Valid Anagram
Difficulty: Easy

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.
*/

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) 
            return false;
        
        unordered_map<char, int> umCharCounts;

        for (int i = 0; i < s.length(); i++) {
            // If counts all equal 0 then strings are anagrams
            umCharCounts[s[i]]++;  
            umCharCounts[t[i]]--;
        }
        
        // Compare counts
        for (auto key : umCharCounts)
            if (key.second)   // If value in pair has value of not 0
                return false;
        
        return true;
    }
};
