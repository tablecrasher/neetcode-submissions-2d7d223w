class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        res = 1
        for i in range(len(s)-1):
            j = i + 1
            window = s[i]
            while j < len(s) and s[j] not in window:
                res = max(res, j-i+1)
                window += s[j]
                j += 1
            i = j
        return res