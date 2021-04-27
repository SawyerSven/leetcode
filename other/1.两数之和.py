#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List
# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, value in enumerate(nums):
            dic[value] = index
        for ri1, value in enumerate(nums):
            ri2 = dic.get(target - value)
            if(ri2 is not None and ri1 != ri2):
                return [ri1, ri2]


# @lc code=end
so = Solution()

so.twoSum([2, 7, 5, 3, 6], 11)
