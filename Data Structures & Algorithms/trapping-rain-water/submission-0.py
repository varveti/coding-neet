class Solution:
    def trap(self, height: List[int]) -> int:
        water = left = 0
        right = len(height) -1 
        leftMax = height[left]
        rightMax = height[right]
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                water = water + (leftMax - height[left])
            else:
                right = right - 1
                rightMax = max(rightMax, height[right])
                water = water + (rightMax - height[right])
        return water