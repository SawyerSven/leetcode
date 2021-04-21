#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vl1 = version1.split('.')
        vl2 = version2.split('.')
        diff = len(vl1) - len(vl2)
        if(diff > 0):
            for i in range(diff):
                vl2.append('0')
        else:
            for i in range(abs(diff)):
                vl1.append('0')
        for i in range(len(vl1)):
            if(int(vl1[i]) > int(vl2[i])):
                return 1
            elif(int(vl1[i]) < int(vl2[i])):
                return -1
        return 0
        
# @lc code=end

so = Solution()

version1 = '1.1.00001.0.1.1'
version2 = '1.1.1.0000.0001.1'

print(so.compareVersion(version1,version2))