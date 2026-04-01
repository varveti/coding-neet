class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for i in range(len(nums)):
            second_num = target - nums[i]
            if second_num in ref and i != ref[second_num]:
                return [min(i, ref[second_num]), max(i, ref[second_num])]
            ref[nums[i]] = i
            print(ref)