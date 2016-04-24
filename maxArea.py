# # Given n non-negative integers a1, a2, ..., an, where each represents a point
#  at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
#   of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
#    forms a container, such that the container contains the most water.
# #
# # Note: You may not slant the container.
# This is also known as the skyline problem.
#optimal solution is O(nlogn)
#solution should involve sorting the heights and another pass
#to get the max x axis difference

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxAR = 0
        count = 0
        while count < len(height):
            for i in range(len(height)-1, count, -1):
                if height[i] > height[count]:
                    minH = height[count]
                else:
                    minH = height[i]
                area = ((i - count) * minH)
                if area < 0:
                    area = area * -1
                if  area > maxAR:
                    maxAR = area
            count = count + 1
        return maxAR
