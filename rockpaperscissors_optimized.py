import random, sys
print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0
count = 0
while True: 
    print('%s Wins, %s Losses, %s Ties ----> %s rounds' %(wins, losses, ties, count))
    while True: 
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        yourmove = input()
        if yourmove == 'q':
            sys.exit()
        if yourmove == 'r' or yourmove == 'p' or yourmove == 's':
            break
        print('Type one of r, p, s, or q')
    
    if yourmove == 'r':
        print('ROCK versus...')
    elif yourmove == 'p':
        print('PAPER versus...')
    elif yourmove == 's':
        print('SCISSORS versus...')
    
    computermove = random.choice(['r','p','s'])
    if computermove == 'r':
        print('ROCK')
    elif computermove == 'p':
        print('PAPER')
    elif computermove == 's':
        print('SCISSORS')

    if yourmove == computermove:
        print('It is a tie')
        ties += 1
    elif yourmove == 'r' and computermove == 's':
        print('You win')
        wins += 1
    elif yourmove == 'p' and computermove == 'r':
        print('You win')
        wins += 1
    elif yourmove == 's' and computermove == 'p':
        print('You win')
        wins += 1
    elif yourmove == 'r' and computermove == 'p':
        print('You lose!')
        losses += 1
    
    elif yourmove == 'p' and computermove == 's':
        print('You lose!')
        losses += 1
    
    elif yourmove == 's' and computermove == 'r':
        print('You lose!')
        losses += 1
    
    count += 1