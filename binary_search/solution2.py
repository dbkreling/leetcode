#!/usr/bin/python

# Set one
nums = [-1,0,3,5,9,12,15]
target = 9

# Set two
# nums = [-1,0,3,5,9,12,15]
# target = -1

start = 0
end = len(nums)-1 # we subtract 1 because it's a 0-indexed array

while start <= end:
    mid = (start + end) // 2
    if nums[mid] == target:
        print(mid)
        exit()
    elif nums[mid] < target:
        start = mid + 1 # we add 1 because mid was already tested
    else:
        end = mid - 1 # we subtract 1 because mid was already tested

print(-1)


