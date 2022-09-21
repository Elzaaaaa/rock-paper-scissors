human_turn = 'rock'
computer_turn = 'scissors'

if human_turn == 'rock' and computer_turn == 'scissors':
    print('human wins!')
elif human_turn == 'paper' and computer_turn == 'rock':
    print('human wins!')
elif human_turn == 'scissors' and computer_turn == 'rock':
    print('human wins!')
if human_turn == 'rock' and computer_turn == 'paper':
    print('computer wins!')
if human_turn == 'paper' and computer_turn == 'scissors':
    print('computer!')
if human_turn == 'scissors' and computer_turn == 'rock':
    print('computer wins!')
if human_turn == computer_turn :
    print('draw!')
