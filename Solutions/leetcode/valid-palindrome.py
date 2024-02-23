class Solution:
    def isPalindrome(self, s: str) -> bool:
        final = ""
        allLetters = list(string.ascii_lowercase + string.ascii_uppercase)
        for letter in s:
            if(letter in allLetters or letter.isdigit()):
                final += letter
        if final.lower() == final.lower()[::-1]:
            return True