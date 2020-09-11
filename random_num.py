import random
import Turtle


n = random.randint(1, 100)
answer = int(input(' '))


count = 0
while answer != n:
    if answer > n:
        print('lower')
    elif answer < n:
        print('higher')

    if answer == n:
        print('You win!')
    elif count == 4:
        print('You lose!')
        break
    answer = int(input(' '))
    count += 1
