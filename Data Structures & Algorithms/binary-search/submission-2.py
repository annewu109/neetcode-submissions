class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        midPos = -1

        while l <= r:
            midPos = int((l + r)/2)
            mid = nums[midPos]

            if mid == target:
                return midPos
            elif mid < target:
                l = midPos + 1
            elif mid > target:
                r = midPos - 1

        return -1