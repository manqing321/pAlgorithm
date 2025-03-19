from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        while len(dict) > 0 :
            vec = []
            for num in dict.keys():
                vec.insert(len(vec), num)

            for num in vec:
                dict[num] -= 1
                if dict[num] == 0:
                    del dict[num]
            
            ans.insert(len(ans), vec)

        return ans

sol = Solution()
nums = [1,3,4,1,2,3,1]
ans = sol.findMatrix(nums)
print(ans)