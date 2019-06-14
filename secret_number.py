from random import randint

tries = str(input('Do you want unlimited tries? Ender \'y\' or \'n\': '))

game = 1
secret_num = randint(1,100)

if tries == 'y':
    while game == 1:
        guess = int(input('Enter a number in the range of 1-100: '))
        if guess < 1 or guess > 100:
            print('Invalid input! Must enter number within range of 1-100')
            quit(0)
        elif guess < secret_num:
            print(guess, 'is less than the secret number')
        elif guess > secret_num:
            print(guess, 'is bigger than the secret number')
        elif guess == secret_num:
            print(guess, 'is the correct answer')
            game = 0

elif tries == 'n':
    usr_tries = randint(1,10)
    print('You have ', usr_tries, 'tries')
    for i in range(usr_tries):
        guess = int(input('Enter a number in the range of 1-100: '))
        print(usr_tries - i -1, 'tries left!')
        if guess < 1 or guess > 100:
            print('Invalid input! Must enter number within range of 1-100')
            quit(0)
        elif guess < secret_num:
            print(guess, 'is less than the secret number')
        elif guess > secret_num:
            print(guess, 'is bigger than the secret number')
        elif guess == secret_num:
            print(guess, 'is the correct answer')
