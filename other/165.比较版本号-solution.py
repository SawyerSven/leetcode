#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)
        while(n1 > p1 or n2 > p2):
            i1, p1 = self.get_next_chunk(version1, n1, p1)
            i2, p2 = self.get_next_chunk(version2, n2, p2)
            if(i1 != i2):
                return 1 if i1 > i2 else -1
        return 0

    def get_next_chunk(self, version, length, pointer):
        if(pointer > length - 1):
            return 0, pointer
        pointer_end = pointer
        while(pointer_end < length and version[pointer_end] != '.'):
            pointer_end += 1
        i = int(version[pointer:pointer_end]) if pointer_end != length - 1 else int(version[pointer:length])
        pointer = pointer_end + 1
        return i, pointer

# @lc code=end

