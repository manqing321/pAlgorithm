from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        seed = 0
        arr_max = 0
        arr_min = 0
        for num in differences:
            seed += num
            arr_max = max(arr_max, seed)
            arr_min = min(arr_min, seed)
        
        arr_range = arr_max - arr_min
        scope = upper - lower

        if scope < arr_range:
            return 0

        return scope - arr_range + 1