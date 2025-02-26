'''
You are given an array non-negative integers height which represent an elevation map.
Each value height[i] represents the height of a bar, which has a width of 1.
Return the maximum area of water that can be trapped between the bars.
'''
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max, suffix_max = [0] * len(height), [0] * len(height)
        r = len(height)
        l_max, r_max = 0, 0

        for l in range(len(height)):
            r -= 1

            prefix_max[l] = l_max
            suffix_max[r] = r_max

            if height[l] > l_max:
                l_max = height[l]
            if height[r] > r_max:
                r_max = height[r]

        level = [0] * len(height)
        for i in range(len(height)):
            level[i] = min(prefix_max[i], suffix_max[i]) - height[i]

        # print(prefix_max)
        # print(suffix_max)
        # print(level)
        return sum(x for x in level if x > 0)

def main():
    solution = Solution()
    height = [0,2,0,3,1,0,1,3,2,1]
    result = solution.trap(height)
    print(result)

if __name__ == "__main__":
    main()