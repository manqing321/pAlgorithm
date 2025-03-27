class Solution:
    def mincost(self, s: str, ch: str) -> int:
        total_cost = 0
        i = 0
        while i < len(s):
            if s[i] == ch:
                j = i
                while j < len(s) and s[j] == ch:
                    j += 1
                left_cost = j + i
                right_cost = len(s) - j + len(s) - i
                total_cost += min(left_cost, right_cost)
                i = j
            else:
                i += 1
        return total_cost

    def minimumCost(self, s: str) -> int:
        return min(self.mincost(s, "0"), self.mincost(s, "1"))

s = "010101"
sol = Solution()
ans = sol.minimumCost(s)
print(ans)
