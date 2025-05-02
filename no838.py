class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = str()
        rear_l_lst = [0] * len(dominoes)
        l_cnt = 0
        for idx in reversed(range(len(dominoes))):
            c = dominoes[idx]
            if c == 'L':
                l_cnt = 1
            elif c == 'R':
                l_cnt = 0
            elif l_cnt > 0:
                rear_l_lst[idx] = l_cnt
                l_cnt += 1
        for num in rear_l_lst:
            print(num, end=" ")
        print()

        r_cnt = 0
        for idx in range(len(dominoes)):
            c = dominoes[idx]
            if c == 'R':
                r_cnt = 1
            elif c == 'L':
                r_cnt = 0
            else:
                if r_cnt == rear_l_lst[idx]:
                    c = '.'
                elif r_cnt != 0 and rear_l_lst[idx] != 0:
                    if r_cnt < rear_l_lst[idx]:
                        c = 'R'
                    else:
                        c = 'L'
                elif r_cnt == 0 and rear_l_lst[idx] != 0:
                    c = 'L'
                elif r_cnt != 0 and rear_l_lst[idx] == 0:
                    c = 'R'
                if r_cnt > 0:
                    r_cnt += 1
            ans = ans + c
        return ans


dominoes = str(".L.R...LR..L..")
ans = Solution().pushDominoes(dominoes)
print(ans)