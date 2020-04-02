''' Antonio Pelayo Mar 1, 2020
Problem: 334 Reverse String
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]'''

def reverseString(s):
  # Space complexity: O(1)
  # Time complexity: O(n)
  i = 0  # Pointers
  j = len(s) - 1

  while i < j:
    # Swap to mirrored index
    s[i], s[j] = s[j], s[i]

    i += 1    # increment pointers
    j -= 1

  return s

a = ['h', 'e', 'l', 'l', 'o']
b = ['H', 'a', 'n', 'n', 'a', 'h']

print(reverseString(a))
print(reverseString(b))