import random
game_status = True
user_points = 0
com_points = 0

def com_turn():
    randnum = random.randint(1,3)
    global com_choice
    if (randnum == 1):
        com_choice = "r"
    elif (randnum == 2):
        com_choice = "p"
    elif (randnum == 3):
        com_choice = "s"
    else:
        print("What the fuck")
        sys.exit()

def score_keep():
    print("The score is: player(",user_points,"), com(",com_points,")")
while game_status == True:
    com_turn()
    user_choice = input("Please choose rock(r), paper(p), or scissors(s): ")
    if user_choice in ("s","p","r"):
        if (user_choice == "s" and com_choice == "r") or (user_choice == "p" and com_choice == "s") or (user_choice == "r" and com_choice == "s"):
            print("The computer has won!")
            com_points += 1
        elif (user_choice == com_choice):
            print("It is a tie")
        else:
            print("The player has won")
            user_points += 1
        score_keep()
    else:
        print("Invalid choice")
