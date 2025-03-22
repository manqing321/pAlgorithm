from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans_row = 0
        ans_cnt = 0
        for row, lst in enumerate(mat):
            cnt = sum(lst)
            if cnt > ans_cnt:
                ans_cnt = cnt
                ans_row = row

        return [ans_row, ans_cnt]

mat = [[0,0,0],[0,1,1]]
sol = Solution()
ans = sol.rowAndMaximumOnes(mat)
print(ans)