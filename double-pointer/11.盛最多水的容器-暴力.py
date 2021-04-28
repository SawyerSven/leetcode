#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
# ! 超时了！！！！！！！！！！！！！！！！
from typing import List
# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        max_height = 0
        while(i < len(height)):
            j = len(height) - 1
            while(j > i):
                curr_height = min(height[j], height[i]) * (j - i)
                if(curr_height > max_height):
                    max_height = curr_height
                j -= 1
            i += 1
        return max_height
# @lc code=end


so = Solution()
so.maxArea([2, 4, 5, 3, 1, 5, 5, 2, 6, 5, 4])
