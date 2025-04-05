from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        size = len(nums)
        beg = 0
        end = 1 << size
        while beg < end:
            flag = beg
            idx = 0
            not_or_sum = 0
            while flag > 0:
                if (flag & 1) == 1:
                    not_or_sum ^= nums[idx]
                flag >>= 1
                idx += 1
            ans += not_or_sum
            beg += 1
        return ans

nums = [5,1,6]
ans = Solution().subsetXORSum(nums)
print(ans)