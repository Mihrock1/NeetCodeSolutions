'''
You are given an array of integers temperatures where temperatures[i] represents the daily
temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer
temperature appears on a future day. If there is no day in the future where a warmer temperature
will appear for the ith day, set result[i] to 0 instead.
'''

from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = deque()

        for i in range(len(temperatures)):

            while bool(stack) and temperatures[stack[-1]] < temperatures[i]:
                popped_element = stack.pop()
                res[popped_element] = i - popped_element

            stack.append(i)

        return res

def main():
    solution = Solution()
    temperatures = [30,38,30,36,35,40,28]
    result = solution.dailyTemperatures(temperatures)
    print(result)

    temperatures = [22,21,20]
    result = solution.dailyTemperatures(temperatures)
    print(result)

if __name__ == "__main__":
    main()