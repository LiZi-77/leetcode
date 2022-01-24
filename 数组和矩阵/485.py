class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_ = 0
        max_ = 0
        for num in nums:
            if num is 0:
                cur_ = 0
            else:
                cur_ += 1
            max_ = max(max_,cur_)
        return max_
