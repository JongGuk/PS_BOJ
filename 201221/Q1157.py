'''알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.'''
word = input().lower() # 모두 소문자로 바꾼다.
check = []
for i in word:
    check.append(ord(i)) # 단어를 아스키코드로 바꿔서 리스트에 넣음

num_spell = []
for j in range(97,123): # 97~122 (알파벳 a~z)가 각각 몇개있는지 셈
    num_spell.append(check.count(j))

num_max_appear_spell = max(num_spell)   # 가장 자주 등장한 횟수를 기록
index_num_max_appear_spell = num_spell.index(max(num_spell)) # 가장 자주 등장한 횟수의 인덱스 확인

del num_spell[index_num_max_appear_spell] # 가장 자주 등장한것을 제거하고, 공동 1위가 있는지 확인
if max(num_spell) == num_max_appear_spell: # 공동 1위가 있으면 ? 출력 (예외처리)
    print("?")
else:
    print(chr(index_num_max_appear_spell+97).upper()) # 공동 1위가 없으면 아까 저장한 인덱스를 통해 알파벳 출력

'''
import sys

n = sys.stdin.readline().rstrip().upper()
t = []

for i in set(n):
    t.append(n.count(i))
idx = [i for i, x in enumerate(t) if x == max(t)]

if len(idx) > 1:
    print('?')
else:
    print(list(set(n))[t.index(max(t))])'''