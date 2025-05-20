from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        selected = []
        def dfs(left: int, right: int):
            if left == 0 and right == 0:
                ans.append(''.join(selected))
                return
            if left > right:
                return
            
            # select left
            if left > 0:
                selected.append('(')
                dfs(left - 1, right)
                selected.pop()
            
            # select right
            if right > 0:
                selected.append(')')
                dfs(left, right - 1)
                selected.pop()

        dfs(n, n)
        return ans

n = 3
ans = Solution().generateParenthesis(n)
for s in ans:
    print(s)