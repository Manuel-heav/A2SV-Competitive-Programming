class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            answer = [1]*(rowIndex + 1)
            temp = self.getRow(rowIndex-1)
            for i in range(1, rowIndex):
                answer[i] = temp[i] + temp[i-1]

            return answer   