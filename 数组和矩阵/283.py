class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i1, i2, l:List[int]) -> List[int]:
            a = l[i1]
            l[i1] = l[i2]
            l[i2] = a
            return l            
        
        first_index = -1
        
        for curr_index in range(len(nums)-1):
            if nums[curr_index] is 0:
                if first_index < 0:
                    first_index = curr_index
                if nums[curr_index+1] is not 0:
                    nums = swap(first_index, curr_index+1,nums)
                    first_index += 1
                 
