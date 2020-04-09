""" Antonio Pelayo April 8, 2020
Problem: 125 Valid Palindrome
Difficulty: Easy

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

def isPal(s):
    S = ''.join(c.lower() for c in s if c.isalnum())
    return S == S[::-1]

def isPalindrome(s):
    answer = ''
    s = s.lower()
    
    # Only add alphabetical letters to answer string
    for c in s:
        if c.isalnum():
            answer += c

    # Is the stripped string equal to its reverse?
    return answer == answer[::-1]

a = 'A man, a plan, a canal: Panama'
b = 'race a car'

print(isPalindrome(a))
print(isPalindrome(b))

print(isPal(a))
print(isPal(b))