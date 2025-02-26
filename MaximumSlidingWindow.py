'''
You are given an array of integers nums and an integer k. There is a sliding window of size k
that starts at the left edge of the array. The window slides one position to the right until
it reaches the right edge of the array.
Return a list that contains the maximum element in the window at each step.
'''
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        def getMaximum(l: int, r: int) -> int:
            maximum = -1000
            while l <= r:
                maximum = max(nums[l], maximum)
                l += 1

            return maximum

        res = [None] * ((len(nums) - k) + 1)
        l, r, maximum = 0, k - 1, -1000

        while r < len(nums):
            maximum = getMaximum(l, r)

            res[l] = maximum

            l += 1
            r += 1

        return res

def main():
    solution = Solution()
    nums = [1,2,1,0,4,2,6]
    k = 3
    result = solution.maxSlidingWindow(nums, k)
    print(result)

if __name__ == "__main__":
    main()