class Solution:
    def findMin(self, nums: List[int]) -> int:
        def findMinRecursive(l, r):
            mid = (l + r) // 2
            if l >= r:
                return nums[l]
            elif nums[mid] > nums[len(nums) - 1]:
                return findMinRecursive(mid + 1, r)
            else:
                return findMinRecursive(l, mid)
                


        l = 0
        r = len(nums) - 1
        return findMinRecursive(l, r)

