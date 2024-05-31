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
        nums.sort()
        a = 0
        b = 0
        for num in nums:
            if a^num == num or a^num == 0:
                a^=num
                continue
            b^=num
        return [a, b]
    
if __name__ == "__main__":
    s = Solution()
    assert s.singleNumber([1,2,1,3,2,5]) in [[3, 5], [5, 3]]
    assert s.singleNumber([0, 1]) in [[0, 1], [1, 0]]
    assert s.singleNumber([-1, 0]) in [[-1,0], [0, -1]]
    assert s.singleNumber([1403617094,-490450406,-1756388866,-967931676,1878401007,1878401007,-74743538,1403617094,-1756388866,-74743538,-490450406,-1895772685]) in [[-967931676, -1895772685], [-1895772685,-967931676]]