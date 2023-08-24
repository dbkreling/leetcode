#!/usr/bin/python

# nums = [1,1,1,3,3,4,3,2,4,2]
nums = [1,2,3,1]

# My solution
# if len(nums) == len(set(nums)): # no duplicates because set does not allow duplicates
#     print("false")
# else:
#     print("true")

# One line
print(len(nums) != len(set(nums)))