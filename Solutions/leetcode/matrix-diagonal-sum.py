class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagSum = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row - col == 0 or row + col == len(mat)-1:
                    diagSum += mat[row][col]
        return diagSum 