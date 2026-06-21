class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        sideLen = [len(matrix[0]), len(matrix) - 1]
        dirIndex = 0

        x = 0
        y = -1

        while sideLen[dirIndex & 1] != 0:
            for _ in range(sideLen[dirIndex & 1]):
                x += directions[dirIndex][0]
                y += directions[dirIndex][1]
                #print(x, y)
                res.append(matrix[x][y])
            
            sideLen[dirIndex & 1] -= 1
            dirIndex += 1
            dirIndex %= 4

        return res
