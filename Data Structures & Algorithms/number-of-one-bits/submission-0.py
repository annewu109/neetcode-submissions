class Solution:
    def hammingWeight(self, n: int) -> int:
        bitVal = 2 ** 32
        bitCount = 0
        while n > 0:
            if n - bitVal >= 0:
                bitCount += 1
                n -= bitVal
            bitVal /= 2
        return bitCount