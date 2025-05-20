from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 1 - 9
        # limit = 9
        ans = []
        selected = []
        def dfs(idx: int, limit: int):
            if limit == 0:
                if sum(selected) == n:
                    ans.append(selected.copy())
                return
            if sum(selected) > n:
                return
                
            # not select
            if idx > limit:
                dfs(idx - 1, limit)

            # select
            selected.append(idx) 
            dfs(idx - 1, limit - 1)
            selected.pop()
        
        dfs(9, k)
        return ans
    
k = 3
n = 9
ans = Solution().combinationSum3(k, n)
for lst in ans:
    for num in lst:
        print(num, end=',')
    print()

