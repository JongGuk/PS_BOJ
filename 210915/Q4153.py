'''A long time ago, the Egyptians figured out that a triangle with sides of length 3, 4, and 5 had a right angle as its largest angle. 
You must determine if other triangles have a similar property.
For each test case, a line containing "right" if the triangle is a right triangle, and a line containing "wrong" if the triangle is not a right triangle.
'''
while True:
    numbers = list(map(int, input().split()))
    if numbers[0] == 0 and numbers[1] == 0 and numbers[2] == 0:
        break
    numbers.sort()
    if numbers[2]**2 == numbers[0]**2 + numbers[1]**2:
        print("right")
    else:
        print("wrong")
    