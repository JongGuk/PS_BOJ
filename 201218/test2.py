import sys
n = int(input())
for i in range(1,n+1):
    a,b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    print(a+b)