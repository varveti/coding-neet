class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        output = []
        for i in range(len(nums)):
            ref[nums[i]] = i

        for i in range(len(nums)):
            second_number = target - nums[i]
            if second_number in ref and ref[second_number] != i:
                return [i, ref[second_number]]