class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        # water = min(left, right)
        # maxWater = 0 
        # maxWater = max(water, maxWater)
        # compare left and right -> move smaller one
        left = 0
        right = len(heights) - 1
        while left < right:
            runmaxArea = (right-left)*min(heights[left], heights[right])
            maxArea = max(maxArea, runmaxArea)
            if heights[left] <=  heights[right]:
                left = left + 1
            else:
                right = right - 1
        return maxArea
            