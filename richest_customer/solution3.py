#!/usr/bin/python

# accounts = [[1,2,3],[3,2,1]]
accounts = [[1,5],[7,3],[3,5]]
# accounts = [[2,8,7],[7,1,3],[1,9,5]]

#Optimization #2
customers = []
for r in accounts:
    customers.append(sum(r))

print(customers)
print(max(customers))