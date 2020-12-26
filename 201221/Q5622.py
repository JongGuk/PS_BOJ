'''Mirko's grandma still uses an ancient pulse dial telephone with
 a rotary dial as shown in the following picture:

For each digit that we want to dial, 
we need to turn the rotary dial clockwise until the chosen digit reaches the finger stop (metal fin).
Then we let go of the dial and wait for it to return to its original position before we can dial another digit.
In our modern, instant gratification world, the dial return often lasts much longer than our patience.
More precisely, dialling the digit 1 takes a total of two seconds, 
while dialling any larger digit takes an additional second for each additional finger circle counting
from 1 to the dialled digit (as shown in the picture).

Mirko's grandma remembers phone numbers by memorizing a corresponding word which, 
when dialled, results in the correct number being dialled. 

When dialling a word, for each letter, we dial the digit which has that letter written next to it on the dial 
(for example, the digit 7 for the letter S). 
For example, the word UNUCIC corresponds to the number 868242. 
Your task is determining, for a given word, the total time required to dial that word.

(input)
The first and only line of input contains a single word consisting of between 2 and 15 (inclusive) uppercase English letters.

(output)
The first and only line of output must contain the required dialling time.
'''
dial = input()
time = 0
for i in dial:
    if i in ['A', 'B', 'C']:
        time += 3
    elif i in ['D', 'E', 'F']:
        time += 4
    elif i in ['G', 'H', 'I']:
        time += 5
    elif i in ['J', 'K', 'L'] :
        time += 6
    elif i in ['M', 'N', 'O'] :
        time += 7
    elif i in ['P', 'Q', 'R', 'S'] :
        time += 8
    elif i in ['T', 'U', 'V'] :
        time += 9
    elif i in ['W', 'X', 'Y', 'Z'] :
        time += 10
print(time)


'''
from string import ascii_uppercase
atoz = list(ascii_uppercase)

이런식으로 하면 편하게 작성 가능.
Alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

'''