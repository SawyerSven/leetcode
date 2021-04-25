#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while(i < len(nums) and len(nums) - 1 - j >= 0):
            if(nums[i] == val):
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                nums.pop()
                continue
            i += 1
        return len(nums)
# @lc code=end


so = Solution()

print(so.removeElement([1, 2, 2, 3, 4, 5, 6, 1, 2, 3, 4, 4], 3))
