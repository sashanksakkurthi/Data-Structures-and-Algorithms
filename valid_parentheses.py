# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


def valid_parentheses(s: str):
    if len(s) == 1:
        return False
    parentheses_pairs = {")": '(', '}': '{', ']': '['}
    parentheses = []
    for i in range(len(s)):
        if s[i] == "{" or s[i] == "(" or s[i] == "[":
            parentheses.append(s[i])
        else:
            if parentheses == []:
                return False
            if parentheses_pairs.get(s[i]) != parentheses[-1]:
                return False
            else:
                parentheses.pop()
        if parentheses == []:
            return True
        else: return False
    

print(valid_parentheses("["))

