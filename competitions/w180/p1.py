''' Antonio Pelayo March 14, 2020
Problem: 5356. Lucky Numbers in a Matrix
Difficulty: Easy

Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix 
in any order.

A lucky number is an element of the matrix such that it is the minimum element 
in its row and maximum in its column.

Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and 
the maximum in its column

Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and 
the maximum in its column.

Example 3:
Input: matrix = [[7,8],[1,2]]
Output: [7]

Constraints:
m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.
'''

def luckyNumbers (matrix):
  m = len(matrix)
  # n = len(matrix[0])
  luckyNums = []
  rowMins = {}    # Length: m, Values: num: colIndex
  
  # Grab largest values in each rows
  for i in range(m):
    # Grab min in row
    rowMins[min(matrix[i])] = matrix[i].index(min(matrix[i]))
     
  # Check if mins are largest in col
  for num in rowMins:       # Iterate through rows
    numColIndex = rowMins[num]
    col = []
    
    # grab col associated with num
    for row in range(m):
      col.append(matrix[row][numColIndex])
      
    # Check if largest in col
    if num == max(col):
      luckyNums.append(num)
         
  return luckyNums


a = [[3,7,8],[9,11,13],[15,16,17]] 
b = [[1,10,4,2],[9,3,8,7],[15,16,17,12]] 
c = [[7,8],[1,2]]

print(luckyNumbers(a))
print(luckyNumbers(b))
print(luckyNumbers(c))