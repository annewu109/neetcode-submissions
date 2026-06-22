class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n == 0:
            return 1
        elif n > 0:
            for _ in range(n):
                res *= x
        else:
            for _ in range(-n):
                res /= x
        return res