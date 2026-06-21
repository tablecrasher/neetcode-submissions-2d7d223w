class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
                
        t_count, window = {}, {}

        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        have, need = 0, len(t_count)
        res, res_len = [-1,-1], float("inf")
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in t_count and window[s[r]] == t_count[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                window[s[l]] -= 1

                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
                 


