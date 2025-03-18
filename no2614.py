from typing import List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        size = len(nums)
        lst = []
        for r in range(0, size):
            col1 = r
            col2 = size - r - 1  
            lst.insert(len(lst), nums[r][col1]) 
            lst.insert(len(lst), nums[r][col2])
        
        def is_primer(num :int) -> bool:
            for i in range(2, num // 2):
                if num % i == 0:
                    return False
            return True
        
        lst = sorted(lst, reverse= True)
        for num in lst:
            if num > 1 and is_primer(num):
                return num
        return 0
    
nums = [[1,2,3],[5,6,7],[9,10,11]]
sol = Solution()
res = sol.diagonalPrime(nums)
print(res)