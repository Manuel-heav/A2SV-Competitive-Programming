class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        ptArray = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                ptArray.append(s[i])
            if s[i] == ")":
                if len(ptArray) > 0 and ptArray[-1] == "(":
                    ptArray.pop()
                else: 
                    return False
            if s[i] == "}":
                if len(ptArray) > 0 and ptArray[-1] == "{":
                    ptArray.pop()
                else: 
                    return False
            if s[i] == "]":
                if len(ptArray) > 0 and ptArray[-1] == "[":
                    ptArray.pop()
                else: 
                    return False
        if len(ptArray) == 0:
            return True