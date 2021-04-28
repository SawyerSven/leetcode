#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        n = 0
        backup = x
        while(x != 0):
            temp = x % 10
            n = n*10 + temp
            x //= 10
        if(n > pow(2, 32)-1):
            return False
        return True if backup == n else False
# @lc code=end


so = Solution()

print(so.isPalindrome(1))
