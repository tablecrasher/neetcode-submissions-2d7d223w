class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t):
            return ""

        t_count, temp_count = {}, {}

        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)

        have, need = 0, len(t_count)
        res_idx, res_len = [-1,-1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            temp_count[c] = 1 + temp_count.get(c, 0)

            if c in t_count and t_count[c] == temp_count[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < res_len:
                    res_idx = [l, r]
                    res_len = r-l+1
                temp_count[s[l]] -= 1
                if s[l] in t_count and temp_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        l, r = res_idx
        return s[l:r+1] if res_len != float("inf") else ""
            
            