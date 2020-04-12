"""Antonio Pelayo April 11, 2020
Problem: 1409 Queries on a Permutation Wtih Key
Difficulty: Medium

Given the array queries of positive integers between 1 and m, you have to 
process all queries[i] (from i=0 to i=queries.length-1) according to the 
following rules:
* In the beginning, you have the permutation P=[1,2,3,...,m].
* For the current i, find the position of queries[i] in the permutation P (indexing 
  from 0) and then move this at the beginning of the permutation P. Notice that the 
  position of queries[i] in P is the result for queries[i].

Return an array containing the result for the given queries.


Example 1:
Input: queries = [3,1,2,1], m = 5
Output: [2,1,2,1] 
Explanation: The queries are processed as follow: 
For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is 2, then we move 3 to the beginning of P resulting in P=[3,1,2,4,5]. 
For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is 1, then we move 1 to the beginning of P resulting in P=[1,3,2,4,5]. 
For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is 2, then we move 2 to the beginning of P resulting in P=[2,1,3,4,5]. 
For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is 1, then we move 1 to the beginning of P resulting in P=[1,2,3,4,5]. 
Therefore, the array containing the result is [2,1,2,1].  

Example 2:
Input: queries = [4,1,2,2], m = 4
Output: [3,1,2,0]

Example 3:
Input: queries = [7,5,5,8,3], m = 8
Output: [6,5,0,7,5]
 
Constraints:
1 <= m <= 10^3
1 <= queries.length <= m
1 <= queries[i] <= m
"""

def processQueries(queries, m):
    indices = []
    P = []
    # Initialize our permutation list
    for i in range(1, m+1):
        P.append(i)
        
    # Go through list of queries
    for i in range(len(queries)):
        Pcopy = P[:]
        move_to_front_val = queries[i]
        P = [move_to_front_val]
            
        # Get index for value
        for j in range(len(Pcopy)):
            if Pcopy[j] == move_to_front_val:
                indices.append(j)
            else:
                P.append(Pcopy[j])    
                    
    return indices
    
a = ([3, 1, 2, 1], 5)
b = ([4, 1, 2, 2], 4)
c = ([7, 5, 5, 8, 3], 8)

print(processQueries(a[0], a[1]))
print(processQueries(b[0], b[1]))
print(processQueries(c[0], c[1]))