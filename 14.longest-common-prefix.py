#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        min_str = min(strs, key=len)
        for i in range(len(min_str)):
            c1 = min_str[i]
            if all(s[i] == c1 for s in strs):
                prefix += c1
            else:
                return prefix
        return prefix
# @lc code=end

