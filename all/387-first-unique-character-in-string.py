''' Antonio Pelayo April 2, 2020
Problem: 387. First Unique Character in a String
Difficulty: Easy

Given a string, find the first non-repeating character in it and return it's 
index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
'''

def firstUniqChar(s):
    counts = {}

    for letter in s:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
        
    # Find first char with count of 1
    for i in range(len(s)):
        if counts[s[i]] == 1:
            return i

    # None were found
    return -1

a = 'leetcode'
b = 'loveleetcode'

print(firstUniqChar(a))
print(firstUniqChar(b))