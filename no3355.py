from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # build a max lst
        lst = [0] * len(nums)

        # diff array: nums[i] - nums[i - 1]
        lst[0] = nums[0]
        for idx in range(1, len(nums)):
            lst[idx] = nums[idx] - nums[idx - 1]

        for pair in queries:
            beg = pair[0]
            end = pair[1]
            lst[beg] -= 1
            if end < len(nums) - 1:
                lst[end + 1] += 1

        seed = 0
        for idx in range(len(lst)):
            seed += lst[idx]
            if seed > 0:
                return False
        return True

def test01():
    nums = [1,0,1]
    queries = [[0,2]]
    ans = Solution().isZeroArray(nums, queries)
    print(ans)

def test02():
    nums = [4,3,2,1]
    queries = [[1,3],[0,2]]
    ans = Solution().isZeroArray(nums, queries)
    print(ans)

test01()
test02()