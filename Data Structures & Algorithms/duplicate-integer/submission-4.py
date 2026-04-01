class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ref = set()
        for num in nums:
            if num not in ref:
                ref.add(num)
            else:
                return True
        return False