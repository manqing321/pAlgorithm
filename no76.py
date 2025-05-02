class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = {}
        for ch in t:
            if not ch in mp:
                mp[ch] = 0
            mp[ch] += 1
        reconds = {}
        left = 0
        ans_idx = 0
        ans_size = 0
        for right in range(len(s)):
            ch = s[right]
            if ch in mp:
                if not ch in reconds:
                    reconds[ch] = 0
                reconds[ch] += 1
            while all(mp[k] <= reconds.get(k, 0) for k in mp) and ((s[left] not in mp) or mp[s[left]] < reconds[s[left]]):
                if s[left] in reconds:
                    reconds[s[left]] -= 1
                left += 1
            if all(mp[k] <= reconds.get(k, 0) for k in mp):
                size =  right - left + 1
                if ans_size == 0 or size < ans_size:
                    ans_size = size
                    ans_idx = left
        ans = str()
        while ans_size > 0:
            ans += s[ans_idx]
            ans_idx += 1
            ans_size -= 1
        return ans
    
s = "ADOBECODEBANC"
t = "ABC"
r = Solution().minWindow(s, t)
print(r)



