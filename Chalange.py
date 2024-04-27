import random

A = random.randint(1,9)
B = int(input('Enter a number between 1 and 10: '))
if A == B:
    print('Right')
else:
    print('Wrong')

while A != B:
    B = int(input('Try again: '))
    if A == B:
        print('Right')
    else:
        print('Wrong')
