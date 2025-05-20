from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(idx: int, selected: List[int], remainder: int, ans: List[List[int]]):
            if remainder == 0:
                ans.append(selected.copy())
                return

            # not select
            if idx > remainder:
                dfs(idx - 1, selected, remainder, ans)

            # select it
            selected.append(idx)
            dfs(idx - 1, selected, remainder - 1, ans)
            selected.pop()
        
        ans = []
        selected = []
        dfs(n, selected, k, ans)
        return ans

n = 4
k = 2
ans = Solution().combine(n, k)
for lst in ans:
    for num in lst:
        print(num, end=',')
    print()
