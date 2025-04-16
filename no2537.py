from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = 0
        mp = {}
        slow = 0
        fast = -1
        while slow < len(nums) - 1:
            while cnt < k and fast + 1 < len(nums):
                fast += 1
                if nums[fast] in mp:
                    mp[nums[fast]] += 1
                else:
                    mp[nums[fast]] = 1
                cnt += mp[nums[fast]] - 1
            if cnt >= k:
                ans += len(nums) - fast
            
            mp[nums[slow]] -= 1
            cnt -= mp[nums[slow]]
            slow += 1

        return ans
        
