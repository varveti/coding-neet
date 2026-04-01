class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        second_num_ref = {}
        for i, num in enumerate(nums):
            second_num = target - num
            print(second_num)
            print(second_num_ref)
            if second_num in second_num_ref and second_num_ref[second_num] != i:
                print([i, second_num_ref[second_num]])
                return [second_num_ref[second_num], i]
            second_num_ref[num] = i
        return []