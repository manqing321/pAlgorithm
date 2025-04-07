from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        max = 0
        for num in nums:
            sum += num
            if num > max:
                max = num
        if sum % 2 == 1:
            return False
        half = sum // 2
        if max > half:
            return False
        dp = [[False] * (half + 1) for _ in nums]
        for r in range(0, len(nums)):
            num = nums[r]
            if r == 0:
                dp[r][num] = True
                continue
            for c in range(0, half + 1):
                if num > c:
                    dp[r][c] = dp[r - 1][c]
                elif num == c:
                    dp[r][c] = True
                else:
                    dp[r][c] = dp[r - 1][c] or dp[r - 1][c - num]

        return dp[len(nums) - 1][half]


lst = [1,5,11,1]
sol = Solution()
ans = sol.canPartition(lst)
print(ans)