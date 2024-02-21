class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:  
        diagDict = defaultdict(list)
        rows = len(mat)
        cols = len(mat[0])
        answer = []
        for i in range(rows):
            for j in range(cols):
                diagDict[i+j].append(mat[i][j])
        for i in range(len(diagDict)):
            if i % 2 == 0:
                diagDict[i].reverse()
                answer.extend(diagDict[i])
            else:
                answer.extend(diagDict[i])
        return answer
                    
        

        