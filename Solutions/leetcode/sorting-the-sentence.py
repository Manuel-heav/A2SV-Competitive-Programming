class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        numArr = []
        wordArr = []
        wordDict = {}
        answer = []
        for i in range(len(words)):
            numArr.append(int(words[i][-1]))
            wordArr.append(words[i][:-1])
        for i in range(len(words)):
            wordDict[numArr[i]] = wordArr[i]
        
        for i in range(1, len(wordDict) + 1):
            answer.append(wordDict[i])
        return " ".join(answer)
        