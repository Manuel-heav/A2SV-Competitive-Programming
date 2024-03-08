class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        gPtr = 0
        sPtr = 0
        counter = 0

        while gPtr < len(g) and sPtr < len(s):
            if g[gPtr] <= s[sPtr]:
                counter += 1
                gPtr += 1
                sPtr += 1
            else:
                sPtr += 1
        return counter
