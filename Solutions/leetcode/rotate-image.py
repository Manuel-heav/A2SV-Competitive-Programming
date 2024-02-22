class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for row in range(len(matrix)):
            for col in range(row, len(matrix[0])):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
            matrix[row].reverse() 
        return matrix
        