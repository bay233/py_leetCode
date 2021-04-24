# 2013.直方图的水量

class Solution:
    def trap(self, height) -> int:
        Sum = sum(height)
        left, rigth = 0, len(height) - 1
        volume, high = 0, 1
        while left <= rigth:
            while left <= rigth and height[left] < high:
                left += 1
            while left <= rigth and height[rigth] < high:
                rigth -= 1
            volume += (rigth - left + 1)
            high += 1
        return volume - Sum