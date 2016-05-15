# Given n non-negative integers representing an elevation map where the width of
#  each bar is 1, compute how much water it is able to trap after raining.
#
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        if len(height) < 2:
            return 0
        leftMax = 0
        rightMax = height[len(height) - 1]
        left = 0
        right = len(height) - 1
        while left <= right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax < rightMax:
                result += leftMax - height[left]
                left = left + 1
            else:
                result += rightMax - height[right]
                right = right - 1
        return result
