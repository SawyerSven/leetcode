#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List
# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        for i in range(len(nums)):
            j, k = i+1, len(nums) - 1
            print(i,j,k)
# @lc code=end

so = Solution()
so.threeSum([-1, 0, 1, 2, -1, -4])
