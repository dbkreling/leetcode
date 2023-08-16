#!/usr/bin/python

nums = [1,2,3,4]
# nums = [-1, 0, 3, 5, 9, 12, 15]
answer = []

print("nums:", [nums[i] for i in range(len(nums))])
print("subsets of nums:", [nums[:i+1] for i in range(len(nums))])
print("sum all the subsets:", [sum(nums[:i+1]) for i in range(len(nums))])