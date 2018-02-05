"""

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number
and for the multiples of five, it should output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        i = 1
        while i < n + 1:
            if i % 5 == 0 and i % 3 == 0:
                res.append("FizzBuzz")
                i += 1
            elif i % 3  == 0:
                res.append("Fizz")
                i+= 1
            elif i % 5 == 0:
                res.append("Buzz")
                i += 1
            else:
                res.append(str(i))
                i += 1
        return res

obj = Solution()
print(obj.fizzBuzz(15))
# ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']