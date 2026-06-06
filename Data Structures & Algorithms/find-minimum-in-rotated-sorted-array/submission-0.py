class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minimum = float("inf")
        while l <= r:
            if nums[l] <= nums[r]:
                return min(minimum, nums[l])
            m = (l+r)//2
            if nums[l] <= nums[m]:
                minimum = min(minimum, nums[l])
                l = m + 1
            elif nums[r] >= nums[m]:
                minimum = min(minimum, nums[m])
                r = m - 1
        return minimum

