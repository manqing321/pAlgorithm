from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        for (idx, num) in enumerate(nums):
            
            # find the range of lower_bound and upper_bound
            # binary find the low_range_begin
            left = idx
            right = len(nums)
            while left + 1 != right:
                mid = (left + right) >> 1
                if num + nums[mid] < lower:
                    left = mid
                else:
                    right = mid
            low_range_begin = right

            # binary find the up_range_end
            left = idx
            right = len(nums)
            while left + 1 != right:
                mid = (left + right) >> 1
                if num + nums[mid] <= upper:
                    left = mid
                else:
                    right = mid
            up_range_end = right

            # increment the scope of range
            ans += up_range_end - low_range_begin

        return ans
    
nums = [1,7,9,2,5]
lower = 11 
upper = 11
res = Solution().countFairPairs(nums, lower, upper)
print(res)