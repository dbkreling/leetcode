#!/usr/bin/python

nums = [-1,0,3,5,9,12,15]
target = 9


# This is a nice solution, but its complexity is not O(log n) (divide and conquer), it's O(n). So see solution2.py
for i, l in enumerate(nums):
    print("index: {}, value: {}".format(i, l))
    if l == target:
        print(i)
        exit()

print(-1)