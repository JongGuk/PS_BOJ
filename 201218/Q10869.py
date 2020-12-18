#첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
a,b = input().split()
a = int(a)
b = int(b)
print("{0}\n{1}\n{2}\n{3}\n{4}".format(a+b, a-b, a*b, a//b, a%b))
