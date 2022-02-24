#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        nums = list(strX)
        if nums[0] == '-':
            return False
        firstIndex = 0
        endIndex = len(nums)-1
        length = len(nums) / 2
        if isinstance(length, float):
            length += 0.5
            length = int(length)
        for i in range(length):
            if int(nums[firstIndex]) - int(nums[endIndex]) == 0:
                firstIndex  += 1
                endIndex -= 1
                continue
            else:
                return False
        return True


# @lc code=end

