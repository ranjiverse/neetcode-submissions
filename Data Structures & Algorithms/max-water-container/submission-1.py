class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights) - 1
        l = 0
        r = length
        res = 0

        while l < r :
            res = max(res, min(heights[l], heights[r]) * (r - l))
            if heights[l] <= heights[r]:
                l = l  + 1
            else :
                r = r - 1
        return res

