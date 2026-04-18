class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = nums.sort()
        out = []
        for i, num in enumerate(nums):
            if(i>0 and num==nums[i-1]):
                continue
            left = i + 1
            right = len(nums)-1
            while left < right:
                run_sum = nums[left]+ nums[right] + num
                if run_sum > 0:
                    right = right - 1
                elif run_sum < 0:
                    left = left + 1
                else:
                    out.append([num, nums[left], nums[right]])
                    left = left + 1
                    #right = right -1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return out

        