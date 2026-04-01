class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for i, num in enumerate(nums):
            second_num = target - num
            if second_num in ref:
                return [ref[second_num], i]
            ref[num] = i
        
            