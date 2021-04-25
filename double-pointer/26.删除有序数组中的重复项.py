#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#
from typing import List
# @lc code=start

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while(i < len(nums) and j < len(nums)):
            if(nums[i] == nums[j]):
                nums.pop(j)
                continue
            i += 1
            j += 1
        return len(nums)
# @lc code=end

so = Solution()

print(so.removeDuplicates([1,1]))
