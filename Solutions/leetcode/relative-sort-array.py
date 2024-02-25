class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sorted_arr = []
        casted_out = [x for x in arr1 if x not in arr2]
        casted_out.sort()
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] in arr1 and arr2[i] == arr1[j]:
                    sorted_arr.append(arr1[j])
                
        sorted_arr.extend(casted_out)
        return sorted_arr
        