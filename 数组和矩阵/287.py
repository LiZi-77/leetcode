class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        helper = [0]*n
        
        for num in nums:
            if helper[num - 1] == 0:
                helper[num - 1] = 1
            else:
                return num
        
