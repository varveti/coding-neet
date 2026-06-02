class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        static_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[static_index] = nums[i]
                static_index += 1
        return static_index