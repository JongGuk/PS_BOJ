'''Mirko works in a sugar factory as a delivery boy. He has just received an order: 
he has to deliver exactly N kilograms of sugar to a candy store on the Adriatic coast. 
Mirko can use two types of packages, the ones that contain 3 kilograms, and the ones with 5 kilograms of sugar.

Mirko would like to take as few packages as possible. 
For example, if he has to deliver 18 kilograms of sugar, he could use six 3-kilogram packages. 
But, it would be better to use three 5-kilogram packages, and one 3-kilogram package, 
resulting in the total of four packages.

Help Mirko by finding the minimum number of packages required to transport exactly N kilograms of sugar.

The first and only line of input contains one integer N (3 ≤ N ≤ 5000).

The first and only line of output should contain the minimum number of packages Mirko has to use. 
If it is impossible to deliver exactly N kilograms, output -1.
'''
N = int(input())
if N == 3 or N == 5:
    result = 1
elif N == 4 or N == 7:
    result = -1
else: 
    num_5kg, remain = divmod(N,5)
    if remain == 0:
        result = num_5kg
    elif remain == 1:
        result = num_5kg+1
    elif remain == 2:
        result = num_5kg+2
    elif remain == 3:
        result = num_5kg+1
    elif remain == 4:
        result = num_5kg+2
print(result)