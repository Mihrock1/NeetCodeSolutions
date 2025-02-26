'''
You are given an array of strings tokens that represents a valid arithmetic expression in
Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
'''

from collections import deque
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = float("nan")
        stack = deque()
        operations = {'+': lambda a, b: int(a) + int(b),
                      '-': lambda a, b: int(a) - int(b),
                      '*': lambda a, b: int(a) * int(b),
                      '/': lambda a, b: int(a) / int(b)}

        for i, t in enumerate(tokens):
            if bool(stack) and t in operations.keys():
                b = stack.pop()
                a = stack.pop()

                res = operations[t](a, b)
            else:
                res = t

            stack.append(int(res))

        return stack.pop()

def main():
    solution = Solution()
    tokens = ["1","2","+","3","*","4","-"]
    result = solution.evalRPN(tokens)
    print(result)

if __name__ == "__main__":
    main()