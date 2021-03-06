''' 
Antonio Pelayo
March 3, 2020

Problem: 122. Best time to buy and sell stock II
Say you have an array for which the ith element is the price of a given stock 
on day i.
Design an algorithm to find the maximum profit. You may complete as many 
transactions as you like (i.e., buy one and sell one share of the stock multiple 
times).
Note: You may not engage in multiple transactions at the same time (i.e., you 
must sell the stock before you buy again).

Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

def maxProfit(prices):
  # Space complexity: O(1)
  # Time complexity: O(n)
  if len(prices) == 0:
    return 0
  profit = 0

  for day in range(1, len(prices)):    # Skip 0 as it has no previous day to compare
    gain = prices[day] - prices[day - 1]

    if gain > 0:
      profit += gain

  return profit

a = [7,1,5,3,6,4]
b = [1,2,3,4,5]
c = [7,6,4,3,1]

print(f'Max profit over {a} is {maxProfit(a)}.')
print(f'Max profit over {b} is {maxProfit(b)}.')
print(f'Max profit over {c} is {maxProfit(c)}.')
