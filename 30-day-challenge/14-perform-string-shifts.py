"""Antonio Pelayo April 14, 2020
Problem: Perform String Shifts
Difficulty: Easy

You are given a string s containing lowercase English letters, and a matrix 
shift, where shift[i] = [direction, amount]:
    * direction can be 0 (for left shift) or 1 (for right shift). 
    * amount is the amount by which string s is to be shifted.
    * A left shift by 1 means remove the first character of s and append it to 
      the end.
    * Similarly, a right shift by 1 means remove the last character of s and 
      add it to the beginning.
    * Return the final string after all operations.

Example 1:
Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"

Example 2:
Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
 

Constraints:
1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100

Hint #1:
Intuitively performing all shift operations is acceptable due to the constraints.
Hint #2:
You may notice that left shift cancels the right shift, so count the total left 
shift times (may be negative if the final result is right shift), and perform it once.
"""
def stringShift(s, shift):
    cummulative_shift = 0

    # Caluclate cumulative shift
    for change in shift:
        if change[0] == 0:
            # Shift left
            cummulative_shift -= change[1]
        else:
            # Shift right
            cummulative_shift += change[1]
                
    # Remove shifts greater than whole string lenght
    cummulative_shift %= len(s)

    # Slice string
    if cummulative_shift == 0:
        pass
    elif cummulative_shift > 0:
        # Shift to right
        slice = len(s) - cummulative_shift
        s = s[slice:] + s[:slice]
    else:
        # Shift to left
        slice = cummulative_shift - len(s)
        s = s[:slice] + s[slice:]
            
    return s

a = {'s': 'abc', 'shift': [[0, 1], [1, 2]]}
b = {'s': 'abcdefg', 'shift': [[1,1],[1,1],[0,2],[1,3]]}

print(stringShift(a['s'], a['shift']))
print(stringShift(b['s'], b['shift']))
