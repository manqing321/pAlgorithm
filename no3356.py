from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if all(num == 0 for num in nums):
            return 0
        diff_arr = [0] * (len(nums) + 1)    # diff array
        diff_idx = 0    # the next query idx
        left = -1
        right = len(queries)

        # left not match, right macth
        while left + 1 != right:
            # include mid
            mid = (left + right) >> 1
            while diff_idx <= mid:
                if diff_idx >= 0:
                    print('left, right ', left, ', ',  right, ' diff_idx ', diff_idx, ', mid ', mid)
                    quer = queries[diff_idx]
                    beg = quer[0]
                    end = quer[1]
                    inc = quer[2]
                    diff_arr[beg] += inc
                    diff_arr[end + 1] -= inc
                diff_idx += 1
            while diff_idx > mid + 1:
                diff_idx -= 1
                quer = queries[diff_idx]
                beg = quer[0]
                end = quer[1]
                inc = quer[2]
                diff_arr[beg] -= inc
                diff_arr[end + 1] += inc
            
            seed = 0
            is_all_match = True
            for idx, num in enumerate(nums):
                seed += diff_arr[idx]
                if seed < num:
                    is_all_match = False
                    break

            if is_all_match:
                right = mid
            else:
                left = mid
            print(f"{mid} {is_all_match}")
        
        if right == len(queries):
            return -1
        return right + 1

def test01():
    nums = [2,0,2]
    queries = [[0,2,1],[0,2,1],[1,1,3]]
    expect = 2
    actual = Solution().minZeroArray(nums, queries)
    print(f'test01 expect: {expect}, actual: {actual}')

def test02():
    nums = [4,3,2,1]
    queries = [[1,3,2],[0,2,1]]
    expect = -1
    actual = Solution().minZeroArray(nums, queries)
    print(f'test02 expect: {expect}, actual: {actual}')

def test03():
    nums = [5]
    queries = [[0,0,5],[0,0,1],[0,0,3],[0,0,2]]
    expect = 1
    actual = Solution().minZeroArray(nums, queries)
    print(f'test03 expect: {expect}, actual: {actual}')

def test04():
    nums = [0]
    queries = [[0,0,5],[0,0,1],[0,0,3],[0,0,2]]
    expect = 0
    actual = Solution().minZeroArray(nums, queries)
    print(f'test04 expect: {expect}, actual: {actual}')

test01()
test02()
test03()
test04()
