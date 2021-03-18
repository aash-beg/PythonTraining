# Stone, Paper, Scissor
import random
options = ['stone', 'paper','scissor']

Cpu_score = 0
user_score= 0
attempt = 0
while True:
    cpu = random.choice(options)
    user = str(input('Your turn :'))
    if user == cpu:
        print("Draw")
    elif cpu == 'stone' and user =='paper':
        user_score += 1
        print ("You won this round")
    elif cpu == 'stone' and user == 'scissor':
        Cpu_score += 1
        print("CPU won this round")
    elif cpu == 'paper' and user == 'scissor':
        user_score += 1
        print("You won this round")
    elif cpu == 'paper' and user == 'stone':
        Cpu_score += 1
        print("CPU won this round")
    elif cpu == 'scissor' and user == 'stone':
        user_score += 1
        print("You won this round")
    elif cpu == 'scissor' and user == 'paper':
        Cpu_score += 1
        print("CPU won this round")

    attempt += 1
    print(f'You : {user}, CPU : {cpu}')
    print(f"Your Score is {user_score}, CPU's score is {Cpu_score}")

    if attempt == 5:
        if user_score > Cpu_score:
            print('You won the game')
        elif user_score < Cpu_score:
            print('CPU won the game')
        elif user_score == Cpu_score:
            print('Game Drawn')
        break