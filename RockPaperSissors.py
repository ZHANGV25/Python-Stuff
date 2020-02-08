import random
userItem = input('(R)ock, (P)aper, or (S)issors? ')
number = random.randint(1, 3)
user_quit = False

def lose():
    print('You lose :( ')
def win():
    print('You win :)  ')
def tie():
    print('Tie. Play again. ')
def i_choose(RPS):
    print(f'I choose {RPS}.')

'''
1 - rock
2 - paper
3 - sissors
'''

if userItem == 'R' and number == 1:
    i_choose('rock')
    tie()
elif userItem == 'R' and number == 2:
    i_choose('paper')
    lose()
elif userItem == 'R' and number == 3:
    i_choose('sissors')
    win()



if userItem == 'S' and number == 1:
    i_choose('rock')
    lose()
elif userItem == 'S' and number == 2:
    i_choose('paper')
    win()
elif userItem == 'S' and number == 3:
    i_choose('sissors')
    tie()



if userItem == 'P' and number == 1:
    i_choose('rock')
    win()
elif userItem == 'P' and number == 2:
    i_choose('paper')
    tie()
elif userItem == 'P' and number == 3:
    i_choose('sissors')
    lose()
