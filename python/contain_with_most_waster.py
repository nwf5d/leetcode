#!/bin/env python
#coding: GBK
# https://oj.leetcode.com/problems/container-with-most-water/submissions/
class Solution:
    # @return an integer
    def maxArea(self, height):
        if len(height) == 0 or len(height) == 1:
            return 0
            
        minNum = min(height[0], height[-1])
        area = minNum * (len(height) - 1)
        if len(height) == 2:
            return area

        if height[1] >= height[-2]:
            return max(area, self.maxArea(height[1:]))
        else:
            return max(area, self.maxArea(height[:-1]))

    def maxArea2(self, height):
        if len(height) <= 1:
            return 0
        left = 0
        right = len(height) - 1

        maxArea = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            area = min(height[left], height[right]) * (right - left)
            if area > maxArea:
                maxArea = area

        return maxArea


if __name__ == '__main__':
    sol = Solution()
    height = [1, 2, 1]
    print sol.maxArea(height)
    print sol.maxArea2(height)
