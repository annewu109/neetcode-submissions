class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            space = 0
            for j in range(i + 1, len(temperatures)):
                space += 1
                if temperatures[j] > temperatures[i]:
                    res.append(space)
                    break
                elif j == len(temperatures) - 1:
                    res.append(0)
        res.append(0)
        return res
