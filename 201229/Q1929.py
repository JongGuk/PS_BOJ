'''M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.'''
M, N = map(int, input().split())
caseArray = list(range(M,N+1))
if M == 1:
    caseArray.remove(1)

for i in range(M,N+1):
    for j in range(2,i):
        if i % j == 0:
            # print(i,"는 소수가 아닙니다.")
            caseArray.remove(i)
            break

for i in caseArray:
    print(i)
