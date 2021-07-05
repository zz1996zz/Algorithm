import collections
import sys
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = 10001

        for price in prices:
            min_price = min(price, min_price)
            profit = max(price - min_price, profit)
        return profit


answer = Solution()
print(answer.maxProfit(prices = [7,1,5,3,6,4]))
print(answer.maxProfit(prices = [7,6,4,3,1]))

