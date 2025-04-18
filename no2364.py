from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        size = len(nums)
        vec = [num - idx for (idx, num) in enumerate(nums)]
        vec.sort()
        i = 0
        cnt = 0
        while i < size:
            val = vec[i]
            j = i + 1
            while j < size and vec[j] == val:
                cnt += j - i
                j += 1
            i = j
        return (size * (size - 1) >> 1) - cnt


nums = [4,1,3,3]
sol = Solution()
ans = sol.countBadPairs(nums)
print(ans)
