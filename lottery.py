
from random import randint

print('Welcome to the Daily 3 and Daily 4 lotteries\n')

#Daily 3
print('Daily 3:\n')
daily_3 = []
for i in range(3):
    x = randint(0, 9)
    daily_3.append(x)

usr_picks = []
a = int(input('Pick your first number 0-9: '))
b = int(input('Pick your second number 0-9: '))
c = int(input('Pick your third number 0-9: '))
usr_picks.extend([a, b, c])

if daily_3 == usr_picks:
    print('You won the lottery!')
    print('Winning numers: ', daily_3)
    print('Your picks: ', usr_picks)
elif daily_3 != usr_picks:
    print('Today is not your day.\n')
    print('Winning numbers: ', daily_3)
    print('Your picks: ', usr_picks)

#Daily 4
print('Daily 4:\n')
daily_4 = []
for i in range(4):
    x = randint(0,9)
    daily_4.append(x)

usr_picks = []
a = int(input('Pick your first number 0-9: '))
b = int(input('Pick your second number 0-9: '))
c = int(input('Pick your third number 0-9: '))
d = int(input('Pick your fourth number 0-9: '))
usr_picks.extend([a, b, c, d])

if daily_4 == usr_picks:
    print('You won the lottery!\n')
    print('Winning numbers: ', daily_4)
    print('Your picks: ', usr_picks)
elif daily_4 !=usr_picks:
    print('Today is not your day.\n')
    print('Winning numbers: ', daily_4)
    print('Your picks: ', usr_picks)
