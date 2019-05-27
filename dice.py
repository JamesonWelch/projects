from random import randint
from time import sleep

games = int(input('Pick the number of times you\'d like to guess the roll of the dice (1-20): '))

round_num = 1
dice_result = {1: 0,
               2: 0,
               3: 0,
               4: 0,
               5: 0,
               6: 0,}
usr_wins = 0

def end_game():
    print('Your results:')
    for k, v in sorted(dice_result.items()):
        print('Dice landed on ', k, ':', v, 'times')
    print('Correct guesses: ', usr_wins)
    print('Average correct guesses: ', round((usr_wins/games * 100), 1), '%')

for i in range(games):
    dice_roll = randint(1, 6)
    print('Round ', round_num, '...')
    usr_guess = int(float(input('Roll the dice. Guess the number from 1-6: ')))
    
    if (usr_guess == type(int)) and (usr_guess >= 1 and usr_guess < 7):
        sleep(3)

        if usr_guess == dice_roll:
            print('You win!')
            usr_wins += 1
        else:
            print('Better luck next time. Dice landed on ', dice_roll)
        round_num += 1
        dice_result[dice_roll] +=1
    else:
        print('Input invalid. Exiting program...')
        print('Process finished with exit code 0')
        break 

if (usr_guess >= 1 and usr_guess < 7):
    end_game()
