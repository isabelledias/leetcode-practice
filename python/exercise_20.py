"""
20. Valid Parentheses

https://leetcode.com/problems/two-sum/description/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid."""

        # If the length of the string is odd, it is not valid
        if len(s)%2 != 0:
            return False
        
        # Create a dictionary with the opening parentheses as keys and the closing parentheses
        dict_key = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        # Create a list with the opening parentheses
        opening_parentheses = []
        for c in s:
            if c in dict_key.keys():
                opening_parentheses.append(c)
                continue
            if opening_parentheses == []:
                # In case we find a closing parentheses without an opening parentheses
                return False
            
            last_parantheses = opening_parentheses.pop()
            if (c != dict_key[last_parantheses]):
                # In case the closing parentheses does not match with the last opening par
                return False
            
        return opening_parentheses == []
        
if __name__ == "__main__":
    # Testes
    s = Solution()
    assert s.isValid("()") == True
    assert s.isValid("()[]{}") == True
    assert s.isValid("(]") == False
    assert s.isValid("{[]}") == True
    assert s.isValid("([)]") == False
