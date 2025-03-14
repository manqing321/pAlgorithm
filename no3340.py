class Solution:
    def isBalanced(self, num: str) -> bool:
        sign = 1
        diff = 0
        for ch in num:
            n = int(ch)
            diff += sign * n
            sign = - sign
        return diff == 0
