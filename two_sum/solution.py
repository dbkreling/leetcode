#!/usr/bin/python

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
# nums = [2,7,11,15]
# target = 9
nums = [3,2,4]
# nums = [3,3]
target = 6

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        total_sum = nums[i] + nums[j]
        if total_sum == target:
            print(i, j)

