#!/usr/bin/python

# accounts = [[1,2,3],[3,2,1]]
accounts = [[1,5],[7,3],[3,5]]
# accounts = [[2,8,7],[7,1,3],[1,9,5]]

customers = []
for m in accounts:
    Sum = 0
    for a in m:
        Sum += a
    customers.append(Sum)

print(customers)
print(max(customers))