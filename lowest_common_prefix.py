#Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from operator import length_hint


def solution(strs:list)->str:
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
        
    
    strs.sort(key=len)
    temp_common_prefix = ""
    for i in range(len(strs[0])):
        if(strs[0][i] == strs[1][i]):
            temp_common_prefix += strs[0][i]
    

    common_prefix = ""
    for i in range(len(strs)-1):
        for j in range(len(temp_common_prefix)):
            if temp_common_prefix[j] == strs[i+1][j]:
                common_prefix += temp_common_prefix[j]     
        temp_common_prefix = common_prefix
        common_prefix = ""
    common_prefix = temp_common_prefix
    return common_prefix


value = solution(["flower","flow","flight"])
print(value)