#!/usr/bin/python

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        arr = [str(x + 1) for x in range(n)]

        for i in range(2, n, 3):
            arr[i] = "Fizz"
        for i in range(4, n, 5):
            arr[i] = "Buzz"
        for i in range(14, n, 15):
            arr[i] = "FizzBuzz"

        return arr

solution=Solution()

print(solution.fizzBuzz(5))
print(solution.fizzBuzz(15))
print(solution.fizzBuzz(100))
