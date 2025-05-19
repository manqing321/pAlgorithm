from typing import List, Optional

class Solution:
    def dfs(self, lst: List[int], dots: int, idx: int, selected: List[int], ans: List[str]):
        if idx == len(lst):
            if len(selected) == 3:
                # verify selected result
                arr = []
                num = 0
                first_bit = True
                for idx, n in enumerate(lst):
                    if not first_bit and num == 0:
                        return
                    first_bit = False
                    num = num * 10 + n
                    if selected.count(idx):
                        arr.append(num)
                        first_bit = True
                        num = 0
                arr.append(num)
                if all(n < 256 for n in arr):
                    s = '.'.join([str(n) for n in arr])
                    if len(s) == len(lst) + 3:
                        ans.append(s)
            return

        # not select
        self.dfs(lst, dots, idx + 1, selected, ans)

        # select idx
        if dots > 0:
            selected.append(idx)
            self.dfs(lst, dots - 1, idx + 1, selected, ans)
            selected.pop() 

    def restoreIpAddresses(self, s: str) -> List[str]:
        lst =  [int(ch) for ch in s]
        ans = []
        selected = []
        self.dfs(lst, 3, 0,selected, ans)
        return ans

def test01():
    s = "25525511135"
    ans = Solution().restoreIpAddresses(s)
    for s in ans:
        print(s, end=",")
    print()

def test02():
    s = "0000"
    ans = Solution().restoreIpAddresses(s)
    for s in ans:
        print(s, end=",")
    print()

def test03():
    s = "101023"
    ans = Solution().restoreIpAddresses(s)
    for s in ans:
        print(s, end=",")
    print()

test01()
test02()
test03()