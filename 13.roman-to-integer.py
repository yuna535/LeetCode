#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        Icount = s.count('I')
        Vcount = s.count('V')
        Xcount = s.count('X')
        Lcount = s.count('L')
        Ccount = s.count('C')
        Dcount = s.count('D')
        Mcount = s.count('M')
        sub = 1*Icount + 5*Vcount + 10*Xcount + 50*Lcount + 100*Ccount + 500*Dcount + 1000*Mcount
            
        if 'IV' in s:
            sub -= 2
        if 'IX' in s:
            sub -= 2
        if 'XL' in s:
            sub -= 20
        if 'XC' in s:
            sub -= 20
        if 'CD' in s:
            sub -= 200
        if 'CM' in s:
            sub -= 200
        
        return sub
# @lc code=end

