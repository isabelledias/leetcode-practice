"""
1404. Number of Steps to Reduce a Number in Binary Representation to One

https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/
"""

class Solution:
    def numSteps(self, s: str) -> int:
        """Given the binary representation of an integer as a string s,
        returns the number of steps to reduce it to 1.
        """
        counter = 0
        while s != '1':
            counter += 1

            # Divides by 2 when the number is even by removing the last 0 in the bit number
            if s[-1] == '0':
                s = s[:-1]
                continue

            # Adds 1 to the number when the number is odd
            idx = s.rfind('0')
            if idx != -1:
                # This covers cases like "1011" and transforms it to "1100"
                s = s[:idx] + '1' + (len(s)-idx-1)*'0'
            else:
                # This covers cases like "111" and transforms it to "1000"
                s = '1' + len(s)*'0'
        return counter
            
            
if __name__ == "__main__":
    # Testes
    assert Solution().numSteps("1101") == 6
    assert Solution().numSteps("10") == 1
    assert Solution().numSteps("1") == 0