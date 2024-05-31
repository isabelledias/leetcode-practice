"""
1. Two Sum

https://leetcode.com/problems/two-sum/description/
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Given an array of integers nums and an integer target, return indices of the
        two numbers such that they add up to target.
        """
        # Iterate through nums, and check if the difference between the target and
        # the current number exists in the rest of the list. If it does, return the
        # indices of the current number and the difference.
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums[i+1:]:
                return [i, nums[i+1:].index(diff)+i+1]
        
if __name__ == "__main__":
    # Testes
    assert Solution().twoSum([2,7,11,15], 9) in [[0,1], [1,0]]
    assert Solution().twoSum([3,2,4], 6) in [[1,2], [2,1]]
    assert Solution().twoSum([3,3], 6) in [[0,1], [1,0]]
    assert Solution().twoSum([-1,-2,-3,-4,-5], -8) in [[2,4], [4,2]]
