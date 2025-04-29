from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        idx_lst = [-1]
        for idx in range(len(nums)):
            if nums[idx] == max_num:
                idx_lst.append(idx)
        left = 1
        max_cnt = 0
        ans = 0
        for right in range(1, len(idx_lst)):
            max_cnt += 1
            while max_cnt > k:
                max_cnt -= 1
                left += 1
            if max_cnt == k:
                ans += (idx_lst[left] - idx_lst[left - 1]) * (nums.size() - idx_lst[right])
        
        return ans
                
