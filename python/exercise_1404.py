"""
1404. Number of Steps to Reduce a Number in Binary Representation to One

https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/
"""

class Solution:
    def numSteps(self, s: str) -> int:
        counter = 0
        while s != '1':
            counter += 1
            if s[-1] == '0':
                s = s[:-1]
                continue

            idx = s.rfind('0')
            if idx != -1:
                s = s[:idx] + '1' + (len(s)-idx-1)*'0'
            else:
                s = '1' + len(s)*'0'
        return counter
            
            
if __name__ == "__main__":
    # Testes
    assert Solution().numSteps("1101") == 6
    assert Solution().numSteps("10") == 1
    assert Solution().numSteps("1") == 0