'''위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 
그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 
숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지
(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.'''
# 1      0 1            1
# 2-7    6 1+6 (N)      6*1 + 1
# 8-19   18 1+18 (3N)   6*3 + 1
# 20-37  36 1+36 (6N)   6*6 + 1
# 38-61  60 1+60 (10N)  6*10 + 1
target = int(input())
n = 1
while True:
    test = 3*(n*(n-1))+ 1 # 계차(6,12,18,...)가 등차수열(6씩 증가)인 수열에서 n번째 An은 Bn-1까지의 합
    if target <= test:
        print(n)
        break
    n+=1
'''
target = math.ceil((target-1)//6)+1
N = 1
print(target)
while True:
    if target <= (N*(N-1)):
        print(N)
        break
    N += 1
'''

'''
result = N/(6(*n^2-n)) + 1



Room_inc = list(range(0,1001,6))
Room = 1
Room_num = []
for i in Room_inc:
    Room += i 
    Room_num.append(Room)
    print(Room_num)
'''