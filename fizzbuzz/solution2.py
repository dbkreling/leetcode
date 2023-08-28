#!/usr/bin/python

n = 15
output = []

for n in range(1, n + 1):
    if n % 15 == 0:
        word = "FizzBuzz"
        output.append(word)
        continue
    if n % 3 == 0:
        word = "Fizz"
        output.append(word)
        continue
    if n % 5 == 0:
        word = "Buzz"
        output.append(word)
        continue
    else:
        word = str(n)
        output.append(word)
        continue

print(output)