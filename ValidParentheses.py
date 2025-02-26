'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
'''

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        parentheses_pairs = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in parentheses_pairs.keys():
                stack.append(c)

            elif c in parentheses_pairs.values():

                if bool(stack) == False:
                    return False

                popped_element = stack.pop()

                if parentheses_pairs[popped_element] != c:
                    return False

        if bool(stack) == True:
            return False

        return True

def main():
    solution = Solution()
    s = "[]"
    result = solution.isValid(s)
    print(result)

    s = "([{}])"
    result = solution.isValid(s)
    print(result)

    s = "[(])"
    result = solution.isValid(s)
    print(result)

if __name__ == "__main__":
    main()