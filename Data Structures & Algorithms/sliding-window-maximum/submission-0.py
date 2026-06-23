class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []
        
        res = []
        l = 0
        for r in range(k-1, len(nums)):
            window = nums[l:r+1]
            res.append(max(window))
            l += 1
        return res
