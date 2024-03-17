class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        p = list(palindrome)
        N = len(p)
        if N == 1:
            return ""
        for i in range(N):
            if p[i] != "a":
                p[i] = "a"
                break
        if p != p[::-1]:
            return "".join(p)


        p = list(palindrome)

        for i in range(N-1, -1, -1):
            if p[i] == "a":
                p[i] = "b"
                break
        return "".join(p)



        