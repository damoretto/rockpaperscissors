#Problem 10: Rock-Paper-Scissors Game
#• Create a simple text-based Rock-PaperScissors game where the player competes against the computer and the computer picks, randomly, rock or paper or scissors
#• You can use any user interface that you like, but the user must be able to continuously enter their choice of rock or paper or scissors
#• Make sure that you attempt to handle all/some error cases
import random

while(True):
    
    computerlist = ['rock', 'paper', 'scissors']
    computermove = random.choice(computerlist)
    
    usermove = str(input("your move! "))
    usermove = usermove.lower()
    
    if computermove == usermove:
        print("opponent's move:", computermove)
        print('Draw!')
        continue
    
    if computermove == 'rock' and usermove == 'paper':
        print("opponent's move:", computermove)
        print('you win!')
        continue
    
    if computermove == 'rock' and (usermove == 'scissors' or 'scissor'):
        print("opponent's move:", computermove)
        print('you lose!')
        continue
    
    if computermove == 'paper' and (usermove == 'scissors' or 'scissor'):
        print("opponent's move:", computermove)
        print('you win!')
        continue
    
    if computermove == 'paper' and usermove == 'rock':
        print("opponent's move:", computermove)
        print('you lose!')
        continue
    
    if computermove == 'scissors' and usermove == 'rock':
        print("opponent's move:", computermove)
        print('you win!')
        continue
    
    if computermove == 'scissors' and usermove == 'paper':
        print("opponent's move:", computermove)
        print('you lose!')
        continue
        
    else:
        print('try again!')
        