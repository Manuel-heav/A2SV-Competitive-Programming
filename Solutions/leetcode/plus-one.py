class Solution(object):
    def plusOne(self, digits):
        text = ""
        finalArr = []
        for i in range(len(digits)):
            text += str(digits[i])
        numAdded = int(text) + 1
        final = str(numAdded)
        for i in range(len(final)):
            finalArr.append(int(final[i]))
        return finalArr

        