class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 1001
        for num in nums:
            if num < res:
                res = num

        return res