# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2

# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3

def climbStairs(n: int) -> int:
    current,previous_current = 1,1
    for i in range(n-1):
        temp = current
        current = current + previous_current
        previous_current = temp
    return current

print(climbStairs(8))