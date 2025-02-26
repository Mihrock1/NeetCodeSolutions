"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions,
in which case the profit would be 0.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
                continue

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit

def main():
    solution = Solution()
    prices = [10,1,5,6,7,1]
    result = solution.maxProfit(prices)
    print(result)

if __name__ == "__main__":
    main()


