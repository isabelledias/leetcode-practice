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

        # Sort the list so that repeated elements are adjacent.
        nums.sort()

        # Initialize the two single numbers to 0.
        a = 0
        b = 0

        # In the following logic we will use XOR to find the two single numbers.
        # Reminder: 1.a XOR a = 0
        #           2.a XOR 0 = 0
        #           3.a XOR b XOR a = b
        for num in nums:
            # By XORing through the elements of the array, the pairs of numbers will cancel
            # out and the single numbers will remain.
            if a^num == num or a^num == 0:
                # This will run until the first single number is found.
                a^=num
                continue
            # This will start running after the first single number is found.
            b^=num
        return [a, b]
    
if __name__ == "__main__":
    s = Solution()
    assert s.singleNumber([1,2,1,3,2,5]) in [[3, 5], [5, 3]]
    assert s.singleNumber([0, 1]) in [[0, 1], [1, 0]]
    assert s.singleNumber([-1, 0]) in [[-1,0], [0, -1]]
    assert s.singleNumber([1403617094,-490450406,-1756388866,-967931676,1878401007,1878401007,-74743538,1403617094,-1756388866,-74743538,-490450406,-1895772685]) in [[-967931676, -1895772685], [-1895772685,-967931676]]