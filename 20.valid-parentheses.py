#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', 
                ']':'[', 
                '}':'{'}

        stack = []
        for char in s:
            if char in pairs and len(stack)>0:
                openingBrace = pairs[char]
                if stack[-1] != openingBrace:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack)==0

# @lc code=end

