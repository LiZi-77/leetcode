class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        
        i = 1
        split = 1
        while i < n :
            left_arr = arr[:i]
            right_arr = arr[i:]
            if max(left_arr) <= min(right_arr):
                return split + self.maxChunksToSorted(right_arr)
            i += 1
        return split
