from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        st = set()
        for i in reversed(range(len(nums))):
            if nums[i] in st:
                return (i + 3) // 3
            else:
                st.add(nums[i])
        return 0
    
nums = [1,2,3,4,2,1,1,1,3,3,5,7]
sol = Solution()
ans = sol.minimumOperations(nums)
print(ans)
