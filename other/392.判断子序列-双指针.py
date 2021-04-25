#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t) 
        # 设置初始的指针位置
        i = j = 0
        # 两个指针的索引均小于字符串长度时，开始遍历
        # 如果s="",则 i = n = 0; 切不会进入循环
        while(i < n and j < m):
            # 判断两个字符是否相等
            if(s[i] == t[j]):
                # 如果两个字符相等，则代表在t[j]位置找到了s[i]
                # 则后移指针i,下一轮循环查找s中下一个字符
                i += 1
            # 无论找到未找到，都要把t的指针j后移一位
            j += 1
            # 循环结束后，如果指针i == 长度n，则代表字符串s中的字符串
            # 在t中全部依次找到，返回true,否则未全部找到，返回False
        return i == n

        # @lc code=end
so = Solution()

print(so.isSubsequence('acb', 'addfcaqwedvb'))
