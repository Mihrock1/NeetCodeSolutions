'''
You are given an integer array piles where piles[i] is the number of bananas in the ith pile.
You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas
and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile
but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.
'''
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinishPiles(k) -> bool:
            hours = 0

            for p in piles:
                hours += math.ceil(p / k)

            return hours <= h

        minK = high = max(piles)  # biggest pile of bananas
        low = 1
        mid = (low + high) // 2

        while high >= low:
            if mid == minK:
                break

            if not canFinishPiles(mid):
                low = mid + 1
                mid = (low + high) // 2
                continue

            if mid < minK:
                minK = mid
                high = mid - 1
                mid = (low + high) // 2
                continue

        return minK

def main():
    solution = Solution()
    piles = [1,4,3,2]
    h = 9
    result = solution.minEatingSpeed(piles, h)
    print(result)

    piles = [25,10,23,4]
    h = 4
    result = solution.minEatingSpeed(piles, h)
    print(result)

if __name__ == "__main__":
    main()
