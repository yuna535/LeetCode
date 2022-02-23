#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for firstIndex, firstNum in enumerate(nums):
            for secondIndex, secondNum in enumerate(nums):
                if firstIndex == secondIndex:
                    continue
                addNum = firstNum + secondNum
                if target == addNum:
                    return [firstIndex, secondIndex]
# @lc code=end

