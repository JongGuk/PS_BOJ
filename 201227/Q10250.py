'''ACM Hotel
Jiwoo, the manager of the ACM Hotel, is about to assign the vacant rooms to the guests upon their arrival. 
According to customers’ survey, the customers prefer the rooms which are close to the main entrance on-walk. 
Jiwoo likes to assign the rooms on this policy. 
Write a program to help Jiwoo on assigning the rooms for the guests.

For simplicity, let’s assume that the ACM hotel is a rectangular shape, 
an H story building with W rooms on each floor (1 ≤ H, W ≤ 99) 
and that the only one elevator is on the leftmost side (see Figure 1). 
Let’s call this kind of hotel as H × W shaped. 
The main entrance is located on the first floor near the elevator. 
You may ignore the distance between the gate and the elevator. 
Also assume that the distances between neighboring rooms are all the same, 
the unit distance, and that all the rooms only in the front side of the hotel.

The rooms are numbered in YXX or YYXX style where Y or YY denotes the number of the floor
and XX, the index of the room counted from the left. 

Therefore the room shaded in Figure 1 should be 305.
The customers do not concern the distance moved in the elevator though the room on the lower floor 
is preferred than that on the higher floor if the walking distance is same. 
For instance, the room 301 is preferred than the room 102 since 
the customer should walk for two units for the latter but one unit, for the former. 
Additionally, the room 2101 is preferred than the room 102.

Your program should compute the room number which should be assigned 
for the N-th guest according to this policy assuming that all the rooms are vacant initially. 
The first guest should be assigned to 101, the second guest to 201, and so on. 
In Figure 1, for example, the 10th guest should be assigned to the room 402 since H = 6.

Your program is to read from standard input. The input consists of T test cases. 
The number of test cases T is given in the first line of the input. 

Each test case consists of a single line containing and integers H, W, and N: 
the number of floors, the number of rooms on each floor, 
and the index of the arrival time of the guest to be assigned a room, respectively, 
where 1 ≤ H, W ≤ 99 and 1 ≤ N ≤ H × W.

Your program is to write to standard output. 
Print exactly one line for each test case. 
The line should contain the room number of the given hotel, where the N-th guest should be assigned.'''
import math

num_test_case = int(input())

for i in range(1,num_test_case+1):
    num_floor, num_room_each_floor, num_guest = map(int, input().split()) # H, W, N
    XX = (num_guest % num_floor)
    YY = str(math.floor(num_guest / num_floor)+1).zfill(2)
    if XX == 0:
        XX = num_floor
        YY = str(num_guest//num_floor).zfill(2)
    print("{0}{1}".format(XX, YY), sep="")