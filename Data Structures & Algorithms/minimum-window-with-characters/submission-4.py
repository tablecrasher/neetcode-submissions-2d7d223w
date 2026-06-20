class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        res = ""
        t_count = [0] * 128
        for c in t:
            t_count[ord(c)] += 1

        for l in range(len(s)):
            if s[l] in t:
                temp_count = [0] * 128
                r = l 
                while (r < len(s) and not all(temp_count[i] >= t_count[i] for i in range(128))):
                    temp_count[ord(s[r])] += 1
                    r += 1
                
                    if all(temp_count[i] >= t_count[i] for i in range(128)) and (len(s[l:r]) < len(res) or res == ""):
                        res = s[l:r]
        return res
                
                


