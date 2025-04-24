from typing import List 

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        size = len(nums)
        mp = { num: 1 for num in nums }
        cnt = len(mp)
        left = 0
        right = 0
        ans = 0
        mp.clear()
        while left < size:
            while right < size and len(mp) < cnt:
                if not nums[right] in mp:
                    mp[nums[right]] = 0
                mp[nums[right]] += 1
                right += 1
            
            if len(mp) == cnt:
                ans += size - right + 1

            mp[nums[left]] -= 1
            if mp[nums[left]] == 0:
                mp.pop(nums[left])
            left += 1

        return ans

nums = [1,3,1,2,2]
ans = Solution().countCompleteSubarrays(nums)
print(ans)