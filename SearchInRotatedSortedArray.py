'''
You are given an array of length n which was originally sorted in ascending order. It has now
been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target
within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2

        while not low > high:
            if nums[mid] == target:
                return mid
            elif low == high:
                return -1

            if nums[mid] < target:
                if nums[low] > nums[mid] and not nums[low] > target:
                    high = mid - 1
                    mid = (low + high) // 2
                    continue
                elif not nums[high] < target:
                    low = mid + 1
                    mid = (low + high) // 2
                    continue
                else:
                    return -1

            elif nums[mid] > target:
                if not nums[low] > target:
                    high = mid - 1
                    mid = (low + high) // 2
                    continue

                elif nums[mid] > nums[high] and not nums[high] < target:
                    low = mid+1
                    mid = (low+high)//2
                    continue

                else:
                    return -1

def main():
    solution = Solution()
    nums = [3,4,5,6,1,2]
    target = 1
    result = solution.search(nums, target)
    print(result)

    nums = [3,5,6,0,1,2]
    target = 4
    result = solution.search(nums, target)
    print(result)

    nums = [5,1,3]
    target = 3
    result = solution.search(nums, target)
    print(result)

    nums = [5, 1, 2, 3, 4]
    target = 1
    result = solution.search(nums, target)
    print(result)

if __name__ == "__main__":
    main()