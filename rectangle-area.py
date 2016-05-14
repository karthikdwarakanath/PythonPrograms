# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner
# as shown in the figure.

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        Area = ((C-A) * (D-B)) + ((G-E) * (H-G))
        if min(G, C) > max(E, A):
            x = (min(G, C) - max(E, A))
        else:
            x = 0
        if min(D, H) > max(B, F):
            y = (min(D, H) - max(B, F))
        else:
            y = 0
        return Area - (x*y)
