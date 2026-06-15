class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        for i in range(1, len(nums)):
            pre[i] *= nums[i - 1] * pre[i - 1]
            post[len(nums) - 1 - i] *= nums[len(nums) - i] * post[len(nums) - i]

        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = pre[i] * post[i]

        return ans