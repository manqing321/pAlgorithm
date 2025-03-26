class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        def ssum (first_elem: int, last_elem: int, cnt: int) -> int:
            return (((first_elem + last_elem) * cnt) // 2)
        if n <= k // 2:
            return ssum(1, n, n)
        else:
            return ssum(1, k // 2, k // 2) + ssum(k, k - 1 + n - k // 2, n - k // 2)

sol = Solution()
ans = sol.minimumSum(5, 4)
print(ans)