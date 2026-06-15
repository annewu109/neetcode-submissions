class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * (len(cost) + 1)
        dp[0], dp[1] = 0, 0

        def find_dp(val):
            if dp[val] != -1:
                return dp[val]
            else:
                dp[val] = min(find_dp(val - 1) + cost[val - 1], 
                              find_dp(val - 2) + cost[val - 2])
                return dp[val]

        return int(find_dp(len(cost)))