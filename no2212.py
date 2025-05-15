from typing import List
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        bobs = [0] * len(aliceArrows)
        max_score = 0
        ans = [0] * len(aliceArrows)
        def dfs(idx, remainder, score):
            nonlocal max_score, ans

            if idx == len(bobs):
                if score > max_score:
                    max_score = score
                    ans = [num for num in bobs]
                return
        
            # not take it
            dfs(idx + 1, remainder, score)

            # take it
            cost = aliceArrows[idx] + 1
            if remainder < cost:
                return
            bobs[idx] = cost
            dfs(idx + 1, remainder - cost, score + idx)
            bobs[idx] = 0

        dfs(0, numArrows, 0)
        return ans

def test01():
    numArrows = 9
    aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
    ans = Solution().maximumBobPoints(numArrows, aliceArrows)
    print(ans)

def test02():
    numArrows = 3
    aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2]
    ans = Solution().maximumBobPoints(numArrows, aliceArrows)
    print(ans)


test01()
test02()