from typing import List, Optional

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(idx: int, selected: List[int], num: str) -> bool:
            def spec_convert(s: str) -> Optional[int]:
                n = int(s)
                if s[0] == '0' and n != 0:
                    return None
                return n
            if idx == len(num) - 1:
                # verify str
                verify_res = True
                if len(selected) < 2:
                    return False
                selected.append(idx)
                i = 0
                for j in range(len(selected) - 2):
                    str1 = num[i: selected[j] + 1]
                    str2 = num[selected[j] + 1: selected[j + 1] + 1]
                    str3 = num[selected[j + 1] + 1: selected[j + 2] + 1]
                    num1 = spec_convert(str1)
                    num2 = spec_convert(str2)
                    num3 = spec_convert(str3)
                    if (num1 is None or num2 is None or num3 is None or num1 + num2 != num3):
                        verify_res = False
                        break
                    i = selected[j] + 1
                selected.pop()
                if verify_res:
                    for num in selected:
                        print(num, end=',')
                    print()
                return verify_res
            
            # not select
            not_select = dfs(idx + 1, selected, num)
            if not_select:
                return True

            # select it
            if len(selected) > 1:
                diff = idx - selected[len(selected) - 1]
                diff_pre = selected[len(selected) - 1] - selected[len(selected) - 2]
                if diff < diff_pre:
                    return False
            
            selected.append(idx)
            select_res = dfs(idx + 1, selected, num)
            selected.pop()
            return select_res

        selected = []
        return dfs(0, selected, num)


def test01():
    num = "112358"
    expect = True
    actual = Solution().isAdditiveNumber(num)
    print(num, " expect: ", expect, ", actual: ", actual)

def test02():
    num = "199100199"
    expect = True
    actual = Solution().isAdditiveNumber(num)
    print(num, " expect: ", expect, ", actual: ", actual)

def test03():
    num = "1023"
    expect = False
    actual = Solution().isAdditiveNumber(num)
    print(num, " expect: ", expect, ", actual: ", actual)

def test04():
    num = "999999999999999999999999"
    expect = False
    actual = Solution().isAdditiveNumber(num)
    print(num, " expect: ", expect, ", actual: ", actual)

def test05():
    num = "199111992"
    expect = True
    actual = Solution().isAdditiveNumber(num)
    print(num, " expect: ", expect, ", actual: ", actual)

def test06():
    num = "011112"
    expect = False
    actual = Solution().isAdditiveNumber(num)
    print(num, " expect: ", expect, ", actual: ", actual)

test01()
test02()
test03()
test04()
test05()
test06()