#loops
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        for k in range(n):
            index = nums[k]
            depth = 0
            while (nums[index] != -1):
                i = nums[index]
                nums[index] = -1
                index = i
                depth += 1
            if (depth > max_len):
                max_len = depth

        return max_len
       
#超时版本 
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        set_list=[]
        max_len = 0

        for k in range(n):
            set_list.append(nums[k])

            index = nums[k]
            while (nums[index] not in set_list):
                set_list.append(nums[index])
                index = nums[index]
            if (len(set_list) > max_len):
                max_len = len(set_list)
            set_list.clear()

        return max_len
