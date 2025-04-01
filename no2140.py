from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        lst = [0] * (len(questions) + 1)
        for idx in reversed(range(len(questions))):
            # if not select idx, then lst[idx + 1]
            unselect = lst[idx + 1]
            # if select idx
            select = questions[idx][0]
            cost = questions[idx][1]
            if idx + cost + 1 < len(questions):
                select += lst[idx + cost + 1]
            lst[idx] = max(unselect, select)
        return lst[0]

arr = [[21,2],[1,2],[12,5],[7,2],[35,3],[32,2],[80,2],[91,5],[92,3],[27,3],[19,1],[37,3],[85,2],[33,4],[25,1],[91,4],[44,3],[93,3],[65,4],[82,3],[85,5],[81,3],[29,2],[25,1],[74,2],[58,1],[85,1],[84,2],[27,2],[47,5],[48,4],[3,2],[44,3],[60,5],[19,2],[9,4],[29,5],[15,3],[1,3],[60,2],[63,3],[79,3],[19,1],[7,1],[35,1],[55,4],[1,4],[41,1],[58,5]]
# arr = [[3,2],[4,3],[4,4],[2,5]]
# arr = [[1,1],[2,2],[3,3],[4,4],[5,5]]
sol = Solution()
ans = sol.mostPoints(arr)
print(ans)
