class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        helper = [0 for i in range(len(nums))]
        for num in nums:
            if helper[num-1] == 0:
                helper[num-1] = 1
            else:
                dup = num
        miss = helper.index(0)+1
        return [dup,miss]
        
