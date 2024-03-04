class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        prev=None
        i=0
        for c in typed:
            if i<len(name) and c==name[i] :
                prev=c
                i+=1
            elif c==prev:
                continue
            else:
                return False
        return i==len(name)


        