'''
You are given an array of length n which was originally sorted in ascending order.
It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning.
Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
'''
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        min_num = float('inf')

        while low < high:
            if nums[low] > nums[high] and nums[mid] > nums[high]:
                low = mid + 1
                mid = (low + high) // 2
                continue

            if nums[mid] < min_num:
                min_num = nums[mid]
                high = mid
                mid = (low + high) // 2
                continue

        return min_num if min_num != float('inf') else nums[low]

def main():
    solution = Solution()
    nums = [3,4,5,6,1,2]
    result = solution.findMin(nums)
    print(result)

    nums = [4,5,0,1,2,3]
    result = solution.findMin(nums)
    print(result)

    nums = [4,5,6,7]
    result = solution.findMin(nums)
    print(result)

    nums = [2,1]
    result = solution.findMin(nums)
    print(result)

if __name__ == "__main__":
    main()