class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [-1] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        def find_dp(val):
            if dp[val] == -1:
                dp[val] = max(find_dp(val - 1), find_dp(val - 2) + nums[val])
            return dp[val]
        
        return find_dp(len(nums) - 1)