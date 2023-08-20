#!/usr/bin/python

# digits = [1,2,3]
digits = [1,9,9]
# digits = [4,3,2,1]
# digits = [9,9]

print("Digits before:", digits)

for i in range(len(digits)-1,-1,-1):
    if digits[i] == 9:
        digits[i] = 0
    else:
        digits[i] += 1
        print("Digits after: ", digits)
        exit()

digits.insert(0,1)
print("Digits after: ", digits)


# Solution 2
# last_digit = digits[-1] + 1

# if last_digit < 9:
#     digits[-1] += 1
# if last_digit == 10:
#     digits.append(0)
#     digits[-2] = 1
# if digits[-2] == 10:
#     digits.append(0)
#     digits[-2] = 0
#     digits[-3] = 1
# print(digits)

# Solution from leetcode users
# for i in range(len(digits)-1, -1, -1):
#     if digits[i] == 9:
#         digits[i] = 0
#     else:
#         digits[i]+=1
#         print(digits)
#         exit()
# digits.append(0)
# digits[0] = 1
# print(digits)
