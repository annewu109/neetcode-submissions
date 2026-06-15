class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        memo = [0] * (n + 1)
        memo[1] = 1
        memo[2] = 2

        def find_memo(val):
            if memo[val] != 0:
                return memo[val]
            else:
                memo[val] = find_memo(val - 1) + find_memo(val - 2)
                return memo[val]

        return find_memo(n)
        