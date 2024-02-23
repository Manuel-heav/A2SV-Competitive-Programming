class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = dict(zip(heights, names))
        sortedVal = list(zipped.keys())
        sortedVal.sort(reverse=True)
        final = []
        for i in range(len(names)):
            final.append(zipped[sortedVal[i]])
        return final