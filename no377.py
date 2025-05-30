from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        lst = [0] * (target + 1)
        for i in range(len(lst)):
            for num in nums:
                if i == num:
                    lst[i] += 1
                if i > num and lst[i - num] > 0:
                    lst[i] += lst[i - num]
        return lst[-1]


def test01():
    nums = [1,2,3]
    target = 4
    expect = 7
    actual = Solution().combinationSum4(nums, target)
    print(f"test01 expect: {expect}, actual: {actual}")

test01()
