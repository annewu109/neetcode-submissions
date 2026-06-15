class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char.lower() for char in s if char.isalnum())

        begin = 0
        end = len(clean) - 1

        while begin < end:
            if clean[begin] != clean[end]:
                return False
            begin += 1
            end -= 1
        return True
