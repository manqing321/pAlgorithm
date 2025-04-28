from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        asum = 0
        left = 0
        for (right, num) in enumerate(nums):
            asum += num
            while asum * (right - left + 1) >= k:
                asum -= nums[left]
                left += 1
            ans += right - left + 1
        return ans