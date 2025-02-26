"""
Given two strings s and t, return the shortest substring of s such that every character in t,
including duplicates, is present in the substring. If such a substring does not exist,
return an empty string "".
You may assume that the correct output is always unique.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count, s_count = {}, {}

        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        required_chars, matched_chars = len(t_count), 0

        l, r, min_start, min_len = 0, 0, 0, float('inf')

        for r, c in enumerate(s):
            s_count[c] = s_count.get(c, 0) + 1

            if c in t_count and t_count[c] == s_count[c]:
                matched_chars += 1

            while matched_chars == required_chars:
                window_len = r - l + 1
                if window_len < min_len:
                    min_len = window_len
                    min_start = l

                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    matched_chars -= 1
                l += 1

        return s[min_start:min_start + min_len] if min_len != float('inf') else ""

def main():
    solution = Solution()
    s = "OUZODYXAZV"
    t = "XYZ"
    result = solution.minWindow(s, t)
    print(result)

    s = "ADOBECODEBANC"
    t = "ABC"
    result = solution.minWindow(s, t)
    print(result)

    s = "a"
    t = "aa"
    result = solution.minWindow(s, t)
    print(result)

    s = "a"
    t = "a"
    result = solution.minWindow(s, t)
    print(result)

if __name__ == "__main__":
    main()