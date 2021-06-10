#
# @lc app=leetcode.cn id=1672 lang=python3
#
# [1672] 最富有客户的资产总量
#
from typing import List

class Solution1:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxAccount = 0
        for account in accounts:
            total = 0
            for number in account:
                total += number
            if total > maxAccount:
                maxAccount = total
        print(maxAccount)
        return maxAccount
                            
# @lc code=start
class Solution:
    def maximumWealth(self,accounts:List[List[int]]) -> int:
        return max(map(sum,accounts))
# @lc code=end

so = Solution()

print(so.maximumWealth([[1,2,3],[3,4,5]]))