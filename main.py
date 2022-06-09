import random
import re
from config import GAME_CHOICES, RULES, scoreboard

def get_user_choice():
    """
    get and validate player input
    """
    user_input = input('Enter your choice (r,p,s): ')
    if user_input not in GAME_CHOICES:
        print('Oops!!, Wrong Choice, Please try again...')
        return get_user_choice()
    return user_input    

def get_system_choice():
    """
    get random choice from Game_choices
    """
    return random.choice(GAME_CHOICES)

def find_winner(user , system):
    """
    get user choice and system choice and compare with rules and return result
    """
    match = {user, system}
    if len(match) == 1:
        return None

    return  RULES[tuple(sorted(match))]

def update_scorboard(result):
    if result['user'] == 3:
        scoreboard['user'] += 1
    else: 
        scoreboard['system'] += 1

    print("#" * 30)
    print("## ",f'user: {scoreboard["user"]}')
    print("## ",f'system: {scoreboard["system"]}')
    print("#" * 30)


def play():
    """
    main play handler
    """
    result = {'user': 0, 'system': 0}
    while result['system'] < 3 and result['user'] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice,system_choice)
        
        if winner == user_choice:
            msg = 'You win'
            result['user'] +=1
        elif winner == system_choice:
            msg = 'You lose'
            result['system'] +=1
        else:
            msg = 'draw'
        print(msg)
    update_scorboard(result)
    play_again = input("Do you want play again(y/n): ")
    if play_again == 'y':
        play()

if __name__ == "__main__":
    play()
