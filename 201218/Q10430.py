#첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
#첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
print((a+b)%c, ((a%c)+(b%c))%c, (a*b)%c, ((a%c)*(b%c)%c), sep="\n")