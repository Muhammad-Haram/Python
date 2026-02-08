# Random number guessing game with python 

import random

random_num = random.randint(1,10)
print(random_num)

tries = 0

while True:
    guess_num = int(input("guess a number between 1 to 10:"))
    if random_num == guess_num:
        tries += 1
        print(f'hurray, you guess a right number in {tries} tries')
        break
    
    elif random_num > guess_num :
        print('guess a little higher')
        tries += 1
    
    elif random_num < guess_num :
        print('guess a little lower')
        tries += 1
    
    else:
        print('sorry, you guess wrong number')
        tries += 1