'''
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise.
That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        s1_count, s2_count = {}, {}

        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        for r, c in enumerate(s2):
            s2_count[c] = s2_count.get(c, 0) + 1

            if r - window_size + 1 > 0:
                l = r - window_size
                s2_count[s2[l]] -= 1

            if all(k in s2_count and s1_count[k] == s2_count[k] for k in s1_count):
                return True

        return False

def main():
    solution = Solution()
    s1 = "abc"
    s2 = "lecabee"
    result = solution.checkInclusion(s1, s2)
    print(result)

    s1 = "abc"
    s2 = "lecaabee"
    result = solution.checkInclusion(s1, s2)
    print(result)

    s1 = "ab"
    s2 = "lecabee"
    result = solution.checkInclusion(s1, s2)
    print(result)

if __name__ == "__main__":
    main()