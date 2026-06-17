import copy

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currentList, total):
            if total == target:
                res.append(copy.deepcopy(currentList))
                return
            elif total > target or i >= len(nums):
                return
            currentList.append(nums[i])
            dfs(i, currentList, total + nums[i])
            currentList.pop()
            dfs(i + 1, currentList, total)
                
            
        
        dfs(0, [], 0)
        return res