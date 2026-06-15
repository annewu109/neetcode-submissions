class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        dp = [-1] * (n + 1)
        offset = 1

        dp[0], dp[1] = 0, 1
        for num in range(1, n + 1):
            if offset * 2 == num:
                offset = num
            dp[num] = 1 + dp[num - offset]
        return dp