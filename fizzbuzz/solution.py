#!/usr/bin/python

n = 15
output = []

for i in range(n):
    if (i+1) % 3 == 0 and (i+1) % 5 != 0:
        word="Fizz"
    elif (i+1) % 5 == 0 and (i+1) % 3 != 0:
        word="Buzz"
    elif (i+1) % 3 == 0 and (i+1) % 5 == 0:
        word="FizzBuzz"
    else:
        word=str(i+1)
    output.append(word)

print(output)