#!/usr/bin/python
nums = [1,2,3,4]
answer = []

for i in range((len(nums))):
    running_sum = 0
    for j in range(i + 1): # from zero till i+1
        running_sum += nums[j]
    answer.append(running_sum)

print(answer)