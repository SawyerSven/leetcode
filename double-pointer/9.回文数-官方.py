#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0 or (x != 0 and x % 10 == 0)):
            return False
        n = 0
        while (x > n):
            n = n * 10 + x % 10
            x //= 10
        return x == n or x == n//10
# @lc code=end


so = Solution()

print(so.isPalindrome(12321))
