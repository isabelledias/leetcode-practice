"""
260. Single Number III

https://leetcode.com/problems/single-number-iii/description/
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """Given an integer array nums, in which exactly two elements appear only once and all
        the other elements appear exactly twice. Find the two elements that appear only once. 
        You can return the answer in any order."""
        double_nums = nums.copy()
        _ = [double_nums.remove(x) for x in set(nums)]
        return list(set(nums) - set(double_nums))
        

if __name__ == "__main__":
    s = Solution()
    assert s.singleNumber([1,2,1,3,2,5]) in [[3, 5], [5, 3]]
    assert s.singleNumber([0, 1]) in [[0, 1], [1, 0]]
    assert s.singleNumber([-1, 0]) in [[-1,0], [0, -1]]