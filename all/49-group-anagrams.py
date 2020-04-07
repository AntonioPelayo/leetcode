""" Antonio Pelayo April 6, 2020
Problem: 49 Group Anagrams
Difficulty: Medium

Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""

def groupAnagams(strs):
    groups = dict()

    for s in strs:
        sortedString = ''.join(sorted(s))

        if sortedString in groups:
            groups[sortedString].append(s)
        else:
            groups[sortedString] = []
            groups[sortedString].append(s)

    return groups.values()


a = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagams(a))