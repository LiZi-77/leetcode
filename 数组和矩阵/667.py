class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = [1]*n
        interval = k
        
        i = 1
        while (interval>0):
            if i%2 ==1:
                ans[i] = ans[i-1] + interval
            else:
                ans[i] = ans[i-1] - interval
            interval -= 1
            i += 1
            
        while (i<n):
            ans[i] = i+1
            i += 1
        return ans
