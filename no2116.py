class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        size = len(s)
        if size % 2 == 1:
            return False
        
        balance = 0
        for i in range(size):
            if locked[i] == '0':
                balance += 1
            else:
                ch = s[i]
                if ch == ')':
                    balance -= 1
                else:
                    balance += 1
            if balance < 0:
                return False
        balance = 0
        for i in (range(size - 1, -1, -1)):
            if locked[i] == '0':
                balance += 1
            else:
                ch = s[i]
                if ch == '(':
                    balance -= 1
                else:
                    balance += 1
            if balance < 0:
                return False
        return True
        

