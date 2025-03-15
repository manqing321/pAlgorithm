class Solution:
    def scoreOfString(self, s: str) -> int:
        ans, pre, num, diff = 0, 0, 0, 0
        for idx, ch in enumerate(s):
            num = ord(ch)
            if idx > 0:
                diff = num - pre
                if diff < 0:
                    ans -= diff
                else:
                    ans += diff
            pre = num
        return ans


sol = Solution()
print(sol.scoreOfString("hello"))
