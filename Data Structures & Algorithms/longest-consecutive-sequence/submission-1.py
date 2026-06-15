class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        ordered_unique = list(dict.fromkeys(sorted(nums)))
        print(ordered_unique)
        ans = 1
        currLen = 1
        for i in range(1, len(ordered_unique)):
            if ordered_unique[i] - 1 == ordered_unique[i - 1]:
                currLen += 1
            else: 
                currLen = 1
            if currLen > ans:
                ans = currLen
        return ans