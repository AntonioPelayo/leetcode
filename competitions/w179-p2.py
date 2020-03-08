''' Antonio Pelayo March 7, 2020
Problem: 1375. Bulb Switcher III 
Difficulty: Medium

There is a room with n bulbs, numbered from 1 to n, arranged in a row from left 
to right. Initially, all the bulbs are turned off.
At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb change 
color to blue only if it is on and all the previous bulbs (to the left) are 
turned on too.
Return the number of moments in which all turned on bulbs are blue.

Example 1:
Input: light = [2,1,3,5,4]
Output: 3
Explanation: All bulbs turned on, are blue at the moment 1, 2 and 4.

Example 2:
Input: light = [3,2,4,1,5]
Output: 2
Explanation: All bulbs turned on, are blue at the moment 3, and 4 (index-0).

Example 3:
Input: light = [4,1,2,3]
Output: 1
Explanation: All bulbs turned on, are blue at the moment 3 (index-0).
Bulb 4th changes to blue at the moment 3.

Example 4:
Input: light = [2,1,4,3,6,5]
Output: 3

Example 5:
Input: light = [1,2,3,4,5,6]
Output: 6

Constraints:
n == light.length
1 <= n <= 5 * 10^4
light is a permutation of  [1, 2, ..., n]
'''

# Contest solution, timelimit exceded on list of length 18295
def numTimesAllBlue1(lights):
  #numsSoFar = [_ for _ in range(1, i+1)]
  indicesSoFar = []
  moments = 0

  for  i in range(len(lights)):     # Iterate over list
    indicesSoFar.append(i + 1)

    # If lights[:i] is a permutation of indicesSoFar, all bulbs blue
    if sorted(lights[:i]) == indicesSoFar[:i]:
      moments += 1

  return moments

# Rehashed solution 
def numTimesAllBlue(light):
  bulb = 1                # Current bulb in list
  moments = 0             # Count of all blue
  bulbsSoFar = set()      # Indices seen so far
     
  for i, j in enumerate(light):
    bulbsSoFar.add(j)

    while bulb in bulbsSoFar:
      bulb += 1

      if i == bulb - 2:
        moments += 1

  return moments

a =[2,1,3,5,4] 
b =[3,2,4,1,5] 
c =[4,1,2,3]
d =[2,1,4,3,6,5] 
e =[1,2,3,4,5,6]

print(numTimesAllBlue(a))
print(numTimesAllBlue(b))
print(numTimesAllBlue(c))
print(numTimesAllBlue(d))
print(numTimesAllBlue(e))
