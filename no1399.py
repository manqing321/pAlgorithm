class Solution:
    def countLargestGroup(self, n: int) -> int:
        dp = [0]
        mp = {}
        ans = 0
        max_cnt = 0
        for _ in range(n):
            inc = True
            for idx in range(len(dp)):
                if inc:
                    dp[idx] += 1
                    if dp[idx] == 10:
                        dp[idx] = 0
                        continue
                    inc = False
                    break
            if inc:
                dp.insert(len(dp), 1)
            bit_sum = sum(dp)
            if not bit_sum in mp:
                mp[bit_sum] = 0
            mp[bit_sum] += 1
            if max_cnt < mp[bit_sum]:
                max_cnt = mp[bit_sum]
                ans = 1
            elif max_cnt == mp[bit_sum]:
                ans += 1
        return ans


            