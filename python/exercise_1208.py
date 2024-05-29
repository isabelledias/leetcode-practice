"""
1208. Get Equal Substrings Within Budget

https://leetcode.com/problems/get-equal-substrings-within-budget/description/?source=submission-noac
"""

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """Returns the maximum length of a substring of s that can be changed to be the same as
          the corresponding substring of t with a cost less than or equal to maxCost.
        """
        # Calculates the cost of each letter beforehand
        change_cost = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        
        # Keeps track of the starting index of a moving window that makes a substring
        starting_idx = 0
        # Walks through the substring making the window as long as possible
        for current_idx in range(len(s)):
            # Subtract the cost of the current letter from the max cost
            maxCost -= change_cost[current_idx]

            # If the cost is negative, shrink the window by moving the starting index
            #  to the next letter, and add the cost of the letter that was removed
            if maxCost < 0:
                maxCost += change_cost[starting_idx]
                starting_idx += 1

        # Return the length of the substring by subtracting the starting index from the
        #  current index and adding 1 since we started counting from zero
        return current_idx - starting_idx + 1
    