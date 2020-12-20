'''Given two integers A and B, A modulo B is the remainder when dividing A by B.
For example, the numbers 7, 14, 27 and 38 become 1, 2, 0 and 2, modulo 3.
Write a program that accepts 10 numbers as input and outputs the number of distinct numbers in the input,
if the numbers are considered modulo 42.

The input will contain 10 non-negative integers, each smaller than 1000, one per line. 
Output the number of distinct values when considered modulo 42 on a single line. '''
mod_result = []
for i in range(10):
    a = int(input())
    mod_result.append(a%42)

mod_result = set(mod_result)
print(len(mod_result))