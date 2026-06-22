class Solution:
    def isHappy(self, n: int) -> bool:
        seenNumbers = set()
        while n not in seenNumbers:
            seenNumbers.add(n)
            place = 10
            newN = 0
            while n > 0:
                digit = n % 10
                n = n // 10
                newN += digit * digit
            n = newN

        if 1 in seenNumbers:
            return True
        return False
