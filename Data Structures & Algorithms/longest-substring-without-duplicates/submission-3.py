class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        substrChars = set()
        pt1 = 0
        pt2 = 0
        res = 0

        while pt2 != len(s):
            if s[pt2] in substrChars:
                while s[pt2] in substrChars:
                    substrChars.remove(s[pt1])
                    pt1 += 1
            substrChars.add(s[pt2])
            res = max(pt2 - pt1 + 1, res)
            pt2 += 1
        
        return res
