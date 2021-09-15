'''
Two integers A and B will given, please print result of A+B.
Input cases consists with several lines.
'''
import sys

lines = sys.stdin.readlines()

for line in lines:
    A, B = map(int, line.split())
    print(A+B)