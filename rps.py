import random

print('ROCK, PAPER, SCISSORS')
win, losses, ties = 0, 0, 0
print(str(win) + ' Wins, ' + str(losses) +' Losses, ' + str(ties) + ' Ties')
while True:
    computer_move = random.choice(['r','p','s'])
    yourmove = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit\n')
    if yourmove == 'q':
        break
    if yourmove == 'p':
        print('PAPER versus...')
        if computer_move == yourmove:
            print('PAPER')
            print('It is a tie')
            ties += 1
        elif computer_move == 'r':
            print('ROCK')
            print('You win!')
            win += 1
        else:
            print('SCISSORS')
            print('You lose!')
            losses += 1
        print(str(win) + ' Wins, ' + str(losses) +' Losses, ' + str(ties) + ' Ties')
    elif yourmove == 'r':
        print('ROCK versus...')
        if computer_move == yourmove:
            print('ROCK')
            print('It is a tie')
            ties += 1
        elif computer_move == 's':
            print('SCISSORS')
            print('You win!')
            win += 1
        else:
            print('ROCK')
            print('You lose!')
            losses += 1
        print(str(win) + ' Wins, ' + str(losses) +' Losses, ' + str(ties) + ' Ties')
    elif yourmove == 's':
        print('SCISSCORS versus...')
        if computer_move == yourmove:
            print('SCISSORS')
            print('It is a tie')
            ties += 1
        elif computer_move == 'p':
            print('PAPER')
            print('You win!')
            win += 1
        else:
            print('ROCK')
            print('You lose!')
            losses += 1
        print(str(win) + ' Wins, ' + str(losses) +' Losses, ' + str(ties) + ' Ties')
    else:
        print("You have made an error somewhere")
        continue
        
        