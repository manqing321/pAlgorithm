from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        sptr = 0
        lstptr = 0
        while sptr < len(s):
            if lstptr < len(spaces) and sptr == spaces[lstptr]:
                ans += ' '
                lstptr += 1
            ans += s[sptr]
            sptr += 1
        return ans

s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
sol = Solution()
res = sol.addSpaces(s, spaces)
print(res)