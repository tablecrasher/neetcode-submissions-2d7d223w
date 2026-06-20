class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window_one = [0] * 26
        window_two = [0] * 26

        for i in range(len(s1)):
            window_one[ord(s1[i]) - ord('a')] += 1
            window_two[ord(s2[i]) - ord('a')] += 1

        if window_one == window_two:
            return True 

        for i in range(len(s1), len(s2)):
            window_two[ord(s2[i]) - ord('a')] += 1
            window_two[ord(s2[i-len(s1)]) - ord('a')] -= 1

            if window_one == window_two:
                return True

        return False

        