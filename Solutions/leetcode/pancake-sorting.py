class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        k = []
        N = len(arr)

        for i in range(N):
            mx = max(arr[:N-i])
            mx_idx = arr.index(mx) + 1

            arr[:mx_idx] = reversed(arr[:mx_idx])
            k.append(mx_idx)
            arr[:N-i] = reversed(arr[:N-i])
            k.append(N-i)
        return k

        