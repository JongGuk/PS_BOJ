'''주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
주어진 수들 중 소수의 개수를 출력한다.
(입력 예)
4
1 3 5 7

(출력 예)
3
'''
num_case = int(input())
caseArray = list(map(int, input().split()))

count = 0
for i in caseArray:
    # print(i)
    for j in range(2,i):
        if i % j == 0:
            count += 1
            # print(i,"는 소수가 아닙니다.")
            break

if 1 in caseArray:
    count += 1
print("{0}".format(num_case-count))


'''24725750
N = int(input())
def primenumber(number, stack):
    if stack == number - 1:
        return True
    if number % stack == 0:
        return False
    else:
        return primenumber(number, stack + 1)

count = 0
N_list = list(map(int,input().split()))
for i in N_list:
    if i == 1:
        continue
    if i == 2:
        count += 1
        continue
    if primenumber(i,2):
        count += 1
print(count)
'''

'''24723600
import sys
from math import sqrt
count = sys.stdin.readline().rstrip()
count_lst = list(map(int,sys.stdin.readline().rstrip().split()))
res = 0
for i in count_lst:
	Bool = True
	if i < 2:
		continue
	for j in range(2,int(sqrt(i))+1):

		if i%j == 0:
			Bool = False
	if Bool:
		res += 1
print(res)
'''