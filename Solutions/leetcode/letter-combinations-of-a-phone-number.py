class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        bucket = []
        myList = {'2': ["a", "b", "c"], 
        '3': ["d", "e", "f"], 
        '4': ["g", "h", "i"], 
        '5': ["j", "k", "l"], 
        '6': ["m", "n", "o"], 
        '7': ["p", "q", "r", "s"], 
        '8': ["t", "u", "v"], 
        '9': ["w", "x", "y", "z"]}


        def backtrack(i):
            if len(bucket) == len(digits):
                ans.append("".join(bucket[:]))
                return

            for j in myList[digits[i]]:
                bucket.append(j)
                backtrack(i+1)
                bucket.pop()
        backtrack(0)
        if digits == "":
            return []
        else:
            return ans



            
