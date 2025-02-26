"""
You are given a string s consisting of only uppercase english characters and an integer k.
You can choose up to k characters of the string and replace them with any other uppercase English character.
After performing at most k replacements, return the length of the longest substring which contains
only one distinct character.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

def main():
    solution = Solution()
    s = "XYYX"
    k = 2
    result = solution.characterReplacement(s, k)
    print(result)

    s = "AAABABB"
    k = 1
    result = solution.characterReplacement(s, k)
    print(result)

if __name__ == "__main__":
    main()

