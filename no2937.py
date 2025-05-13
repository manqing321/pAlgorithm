class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        def find_core(source: str, target: str) -> int:
            idx = 0
            min_len = min(len(source), len(target))
            while idx < min_len:
                if source[idx] == target[idx]:
                    idx += 1
                else:
                    break
            return idx
        lens = [len(s1), len(s2), len(s3)]
        max_len = min(find_core(s1, s2), find_core(s2, s3))
        if max_len == 0:
            return -1
        else:
            methods = [l - max_len for l in lens]
            return sum(methods)

def test01():
    s1 = "abc"
    s2 = "abb"
    s3 = "ab"
    s = Solution().findMinimumOperations(s1, s2, s3)
    print(s)
def test02():
    s1 = "dac"
    s2 = "bac"
    s3 = "cac"
    s = Solution().findMinimumOperations(s1, s2, s3)
    print(s)
def test03():
    s1 = "a"
    s2 = "a"
    s3 = "a"
    s = Solution().findMinimumOperations(s1, s2, s3)
    print(s)
def test04():
    s1 = "a"
    s2 = "aabc"
    s3 = "a"
    s = Solution().findMinimumOperations(s1, s2, s3)
    print(s)

test01()
test02()
test03()
test04()

