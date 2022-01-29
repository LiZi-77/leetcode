class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # the degree of the array
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
                
        degree = max(dic.values())
        target = []
        for k, v in dic.items():
            if v == degree:
                target.append(k)
                
        n = len(nums)
        length = n+1
        reversed_nums = nums[::-1]
        
        
        for k in target:
            first_index = nums.index(k)
            final_index = reversed_nums.index(k)
            if (n - first_index - final_index) < length:
                length = n - first_index - final_index
        return length
