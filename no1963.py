class Solution:
    def minSwaps(self, s: str) -> int:
        diff = 0
        for ch in s:
            if ch == '[':
                diff += 1
            elif diff > 0:
                diff -= 1
        return (diff + 1) // 2
    
sol = Solution()
ans = sol.minSwaps("]]][[[")
print(ans)