class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target:
                low = mid + 1
            elif matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                high = mid - 1

        row = high

        lowcol = 0
        highcol = len(matrix[0]) - 1

        while lowcol <= highcol:
            print(lowcol, highcol)
            mid = (lowcol + highcol) // 2
            if matrix[row][mid] < target:
                lowcol = mid + 1
            elif matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                highcol = mid - 1
        return False


