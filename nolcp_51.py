from typing import List

class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int) -> int:
        max_delicious = 0
        cooks = [0] * len(cookbooks)
        def dfs(idx: int):
            nonlocal max_delicious
            if idx == len(cooks):
                satiety = 0
                delicious  = 0
                for cook_idx, cook_cnt in enumerate(cooks):
                    delicious += cook_cnt * attribute[cook_idx][0]
                    satiety += cook_cnt * attribute[cook_idx][1]
                if satiety >= limit and delicious > max_delicious:
                    max_delicious = delicious
                return
            
            cnt = 0
            while cnt < 2:
                material_cost = [0] * len(materials)
                for mat_idx, single_cost in enumerate(cookbooks[idx]):
                    material_cost[mat_idx] = cnt * single_cost
                if all(cost <= materials[mat_idx] for mat_idx, cost in enumerate(material_cost)):
                    for mat_idx, cost in enumerate(material_cost):
                        materials[mat_idx] -= cost
                    old_cnt = cooks[idx]
                    cooks[idx] = cnt
                    dfs(idx + 1)
                    for mat_idx, cost in enumerate(material_cost):
                        materials[mat_idx] += cost
                    cooks[idx] = old_cnt
                else:
                    break
                cnt += 1

        dfs(0)
        return max_delicious

# materials = [3,2,4,1,2] 
# cookbooks = [[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1,0]] 
# attribute = [[3,2],[2,4],[7,6]] 
# limit = 5
materials = [10,10,10,10,10] 
cookbooks = [[1,1,1,1,1],[3,3,3,3,3],[10,10,10,10,10]] 
attribute = [[5,5],[6,6],[10,10]] 
limit = 1
ans = Solution().perfectMenu(materials, cookbooks, attribute, limit)
print(ans)
            
        