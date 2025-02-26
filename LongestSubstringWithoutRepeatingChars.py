"""
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_longst_substr = 0
        len_substr = 0
        longst_str = set()

        l, r = 0, 0

        while r < len(s):
            if s[r] not in longst_str:
                longst_str.add(s[r])
                len_substr += 1
            else:
                longst_str.remove(s[l])
                l += 1
                len_substr -= 1
                continue

            if len_substr > len_longst_substr:
                len_longst_substr = len_substr

            r += 1

        return len_longst_substr

def main():
    solution = Solution()
    s = "zxyzxyz"
    result = solution.lengthOfLongestSubstring(s)
    print(result)

    s = "xxxx"
    result = solution.lengthOfLongestSubstring(s)
    print(result)

    s = "abcabcbb"
    result = solution.lengthOfLongestSubstring(s)
    print(result)

    s = "pwwkew"
    result = solution.lengthOfLongestSubstring(s)
    print(result)

if __name__ == "__main__":
    main()


