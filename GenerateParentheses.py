'''
You are given an integer n. Return all well-formed parentheses strings that you can generate
with n pairs of parentheses.
'''

from collections import deque
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = deque()

        def permute(open_count, close_count):
            if open_count == close_count == n:
                res.append("".join(stack))
                return

            if open_count < n:
                stack.append('(')
                permute(open_count + 1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(')')
                permute(open_count, close_count + 1)
                stack.pop()

        permute(0, 0)
        return res

def main():
    solution = Solution()
    n = 1
    result = solution.generateParenthesis(n)
    print(result)

    n = 3
    result = solution.generateParenthesis(n)
    print(result)

if __name__ == "__main__":
    main()