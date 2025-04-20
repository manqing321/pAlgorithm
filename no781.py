from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        mp = {}
        ans = 0
        for answer in answers:
            num = answer + 1
            if not num in mp:
                mp[num] = 1
                continue
            if mp[num] == num:
                ans += num
                mp[num] = 0
            mp[num] += 1
        for num in mp.keys():
            ans += num
        return ans

nums = [1,1,2]
ans = Solution().numRabbits(nums)
print(ans)