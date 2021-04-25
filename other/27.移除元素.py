#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0;
        while(i<len(nums)):
            if(nums[i] == val):
                nums.pop(i)
                continue
            i += 1
        return len(nums)
            
# @lc code=end

so = Solution()

print(so.removeElement([0,1,2,2,3,0,4,2], 2))