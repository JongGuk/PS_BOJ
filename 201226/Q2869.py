'''There is a snail on the ground. 
It wants to climb to the top of a wooden pole with the height of V meters,
measuring from the ground level. In one day it can climb A meters upwards, 
however during each night it sleeps, sliding B meters back down. 
Determine the number of days it needs to climb to the top. 

The first and only line of input contains three integers separated by a single space: 
A, B, and V (1 ≤ B < A ≤ V ≤ 1 000 000 000), with meanings described above. 
The first and only line of output must contain the number of days that the snail needs to reach the top. '''
import math
A, B, V = map(int, (input().split()))

n = math.ceil((V-A)/(A-B))+1
print(n)
'''


if net_climb_per_day >= V:
    req_day = 1
else:
    req_day = math.ceil(V/(net_climb_per_day))


print(req_day)
'''