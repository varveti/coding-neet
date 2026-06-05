class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ref = {}
        for num in nums:
            if num not in ref:
                ref[num] = 1
            else:
                ref[num] += 1
        print(ref)
        return max(ref, key=ref.get)