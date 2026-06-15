class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = [1, len(numbers)]
        currSum = numbers[ans[0] - 1] + numbers[ans[1] - 1]
        while currSum != target:
            if currSum < target:
                ans[0] += 1
            else:
                ans[1] -= 1
            currSum = numbers[ans[0] - 1] + numbers[ans[1] - 1]

        return ans