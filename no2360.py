from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        ans = 0
        lst = [0] * len(edges)
        label = 0
        for i in range(0, len(edges)):
            if lst[i] > 0:
                continue
            pos = i
            core_label = label
            while pos != -1:
                core_label += 1
                if lst[pos] > 0:
                    if lst[pos] > label:
                        ans = max(ans, core_label - lst[pos])
                    break
                lst[pos] = core_label
                pos = edges[pos]
            label = core_label
        return ans
    