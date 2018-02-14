print('Created by Anitha Sri S')
loose = 'The Computer Wins'
win = 'You Win!!'
lives = 5
score = 0
drew = 0
computer_lives = 5
password_list = []
while True:
    print('Enter Username and Password')
    username = input('Please enter your Username:  ')
    password = input('Please enter your Password:  ')
    search_file = open('accounts.txt','r')
    for line in search_file:
        password_list.append(line.strip())
        if username and password in password_list:
            print('Loading...')
            import time
            time.sleep(2)
            print('Access Granted')
            time.sleep(1)
            start_style='''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     ___                  ______________     ______________     _______________     ____      ___                                            
    ¦   ¦                ¦              ¦   ¦              ¦   ¦               ¦   ¦    ¦    /   /                                           
 /------------------     ¦     ___      ¦   ¦  __________  ¦   ¦  _____________¦   ¦    ¦   /   /                                            
/            \     ¦     ¦    ¦   ¦     ¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦  /   /                                             
¦       ------------     ¦    ¦___¦   __¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦_/   /                                              
¦       ------------     ¦           \      ¦ ¦          ¦ ¦   ¦ ¦                 ¦         /                                               
¦            \     ¦     ¦    ¦\      \     ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦\   \                                               
¦       ------------     ¦    ¦ \      \    ¦ ¦__________¦ ¦   ¦ ¦_____________    ¦    ¦ \   \                                              
¦       ------------     ¦    ¦  \      \   ¦              ¦   ¦               ¦   ¦    ¦  \   \                   ___  ___  ___  ___    
¦            \     ¦     ¦____¦   \______\  ¦______________¦   ¦_______________¦   ¦____¦   \___\                 ¦   ¦¦   ¦¦   ¦¦   ¦       
¦       ------------                                                                                          ___ ¦   ¦¦   ¦¦   ¦¦   ¦       
\       ------------ ___________     _______________     ___________     ___________     _____________       ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
 \           \     /¦   _____   ¦   ¦     _____     ¦   ¦   _____   ¦   ¦           ¦   ¦             ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
  \---------------/ ¦  ¦     ¦  ¦   ¦    ¦_____¦    ¦   ¦  ¦     ¦  ¦   ¦    _______¦   ¦     ___     ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
                    ¦  ¦_____¦  ¦   ¦     _____     ¦   ¦  ¦_____¦  ¦   ¦   ¦           ¦    ¦   ¦    ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
                    ¦    _______¦   ¦    ¦     ¦    ¦   ¦    _______¦   ¦   ¦_____      ¦    ¦___¦   _¦      \                       /       
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦    _____¦     ¦           \         \                     /        
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦   ¦_______    ¦    ¦\      \         \                   /         
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦           ¦   ¦    ¦ \      \         \                 /                                _____
                    ¦___¦           ¦____¦     ¦____¦   ¦___¦           ¦___________¦   ¦____¦  \______\         \_______________/                                /     /
                                                                                                                                                                 /     /
 ______________     _______________     ____     ______________     ______________     ______________     _____________     ______________                    /     /
¦   ___________¦   ¦               ¦   ¦    ¦   ¦   ___________¦   ¦   ___________¦   ¦              ¦   ¦             ¦   ¦   ___________¦    ________    /     /
¦  ¦               ¦  _____________¦   ¦    ¦   ¦  ¦               ¦  ¦               ¦  __________  ¦   ¦     ___     ¦   ¦  ¦               /          /     /
¦  ¦___________    ¦ ¦                 ¦    ¦   ¦  ¦___________    ¦  ¦___________    ¦ ¦          ¦ ¦   ¦    ¦   ¦    ¦   ¦  ¦___________   ¦         /     /
¦____________  ¦   ¦ ¦                 ¦    ¦   ¦____________  ¦   ¦____________  ¦   ¦ ¦          ¦ ¦   ¦    ¦___¦   _¦   ¦____________  ¦  ¦       /     /
             ¦ ¦   ¦ ¦                 ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦          ¦ ¦   ¦           \                  ¦ ¦  ¦               __________________
             ¦ ¦   ¦ ¦_____________    ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦__________¦ ¦   ¦    ¦\      \                 ¦ ¦  ¦                                 ¦
 ____________¦ ¦   ¦               ¦   ¦    ¦    ____________¦ ¦    ____________¦ ¦   ¦              ¦   ¦    ¦ \      \    ____________¦ ¦  ¦               __________________¦
¦______________¦   ¦_______________¦   ¦____¦   ¦______________¦   ¦______________¦   ¦______________¦   ¦____¦  \______\  ¦______________¦  ¦______________¦

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
            rules_style='''
---------------------------------------
Live Rules:
You start with 5 lives.
If you win you get a extra live.
If you loose you loose a live.
If you draw the lives stay the same.
----------------------------------------
'''
            play_rules = '''
---------------------------------------------
--> To see a list of rules type 'rules'.
--> To see your lives, type 'display lives'.
--> To see your score, type 'display score'.
--> To see your drew, type 'display drew'.
--> Type 'exit' to leave the game.
----------------------------------------------
'''
            play = '''
-----------------------------------------
The computer has lives as well.
Can you beat the computer?
Good Luck!!
-----------------------------------------
'''
            print(start_style)
            time.sleep(2)
            print(rules_style)
            i = input("Type 'enter' to continue ")
            if i=='enter':
                print(play_rules)
            i = input("Type 'enter' to continue ")
            if i == 'enter':
                print(play)
            while True:
                rps = input("Rock, Paper, Scissors?  ")
                rps = rps.title()
                import random
                computer = ("rock", "paper", "scissors")
                computer = random.choice(computer)
                # rock if statments
                if rps == "Rock" and computer == "paper":
                    print("The computer chose", computer)
                    print("")
                    print(loose)
                    print("")
                    lives -= 1
                if rps == "Rock" and computer == "scissors":
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    print("")
                    score += 1
                    # paper if statements
                if rps == "Paper" and computer == "rock":
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    computer_lives -= 1
                    print("")
                    score += 1
                if rps == "Paper" and computer == "scissors":
                    print("The computer choose", computer)
                    print("")
                    print(loose)
                    print("")
                    lives -= 1
                # scissor if statements
                if rps == "Scissors" and computer == "paper":
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    computer_lives -= 1
                    print("")
                    score += 1
                if rps == "Scissors" and computer == "rock":
                    print("The computer choose", computer)
                    print("")
                    print(loose)
                    print("")
                    lives -= 1
                # duplicates
                if rps == "Rock" and computer == "rock":
                    print("The computer choose", computer)
                    print("")
                    print("You Drew")
                    print("")
                    drew += 1
                if rps == "Paper" and computer == "paper":
                    print("The computer choose", computer)
                    print("")
                    print("You Drew")
                    print("")
                    drew += 1
                if rps == "Scissors" and computer == "scissors":
                    print("The computer choose", computer)
                    print("")
                    print("You Drew")
                    print("")
                    drew += 1
                # system
                if rps == "Rules":
                    print("Rules:")
                    print("-Rock looses against Paper")
                    print("-Rock beats Scissors")
                    print("-Paper beats Rock")
                    print("-Paper looses against Scissors")
                    print("-Scissors beats Paper")
                    print("-Scissors looses against Rock")
                if rps == "Display Lives":
                    print(lives)
                if rps == "Display Score":
                    print(score)
                if rps == "Display Drew":
                    print(drew)
                # lives
                if lives == 0:
                    print('YOU LOST!')
                    print("Thanks for playing.")
                    print("You have run out of lives")
                    print("You got", score, "correct")
                    print("You drew", drew, "times")
                    stop = input("Press enter to exit.")
                    exit()
                if computer_lives == 0:
                    print("Thanks for playing.")
                    print("The computer lost all it's lives.")
                    print('YOU WIN!!')
                    print("You got", score, "correct")
                    print("You drew", drew, "times")
                    stop = input("Press enter to exit.")
                    exit()
                # exit
                if rps == "Exit":
                    break
    if username != line and password != line:
        print("Your username or password is incorrect.")

