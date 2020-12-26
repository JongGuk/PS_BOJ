'''In 1949 the Indian mathematician D.R. Kaprekar discovered a class of numbers called self-numbers. 
For any positive integer n, define d(n) to be n plus the sum of the digits of n. 
(The d stands for digitadition, a term coined by Kaprekar.) 

For example, d(75) = 75 + 7 + 5 = 87. Given any positive integer n as a starting point, 
you can construct the infinite increasing sequence of integers n, d(n), d(d(n)), d(d(d(n))), .... 

For example, if you start with 33, the next number is 33 + 3 + 3 = 39, 
the next is 39 + 3 + 9 = 51, the next is 51 + 5 + 1 = 57, and so you generate the sequence
33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...

The number n is called a generator of d(n). 
In the sequence above, 33 is a generator of 39, 39 is a generator of 51, 51 is a generator of 57, and so on. 
Some numbers have more than one generator: for example, 101 has two generators, 91 and 100.

A number with no generators is a self-number.
There are thirteen self-numbers less than 100: 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, and 97.
Write a program to output all positive self-numbers less than 10000 in increasing order, one per line.'''
def d(n):
    non_self_num = []
    self_num = list(range(1,n+1)) # 1부터 n까지의 셀프 넘버 후보군을 리스트로 저장
    for i in range(1,n+1):
        result = sum([int(j) for j in str(i)]) + int(i)
        #print("{0}의 결과:{1}".format(i, result))
        non_self_num.append(result) # d 연산 결과들을 셀프 넘버가 아닌것으로 지정
        if result in self_num:      # list.remove 의 경우 list 내에 없는 값을 지우려고 하면 에러를 출력하기 때문에 if로 검사
            self_num.remove(result) # 셀프 넘버 후보군에서 셀프 넘버가 아닌것을 추려냄
                   
    for i in self_num:
        print(i)

d(10000)