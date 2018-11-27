import random as r
import time
import überschrift
shoot_direction = ["left", "right", "middle"]
ki_score  = 0
pl_score  = 0
n_penalties = 0

überschrift.titel()

def penalty_pl():
    global n_penalties
    global pl_score
    n_penalties = n_penalties +1
    pl_directionshoot = input("Where do you want to shoot?   ").lower()
    while True:
        if pl_directionshoot != shoot_direction:
            print("incorrect direction")
            pl_directionshoot = input("Where do you want to shoot?   ").lower()
        else:
            False
            pl_directionshoot = shoot_direction
            ki_jumpdirection  = r.choice (shoot_direction)
            print("\n")
            print(f"The Goalkeeper is jumping {ki_jumpdirection}")
            if pl_directionshoot == "left" and ki_jumpdirection =="right":
                print("Keeper saved the ball ! NO GOAL")
            elif pl_directionshoot == "right" and ki_jumpdirection =="left":
                print("Keeper saved the ball ! NO GOAL")
            elif pl_directionshoot == "middle" and ki_jumpdirection =="middle":
                print("Keeper saved the ball ! NO GOAL")
            else:
                print("GOOOAAAL, nice shot !")
                pl_score = pl_score +1
        
def penalty_ki():
    global n_penalties
    global ki_score
    n_penalties = n_penalties +1
    ki_directionshoot = r.choice (shoot_direction)
    pl_jumpdirection  = input("Where do you want to dive?   ").lower()
    print("\n")
    print(f"The shot is going to the {ki_directionshoot}")
    if ki_directionshoot == "left" and pl_jumpdirection =="right":
        print("You saved the ball! Great Keeper skills! NO GOAL")
    elif ki_directionshoot == "right" and pl_jumpdirection =="left":
        print("Wow, what a save! NO GOAL")
    elif ki_directionshoot == "middle" and pl_jumpdirection =="middle":
        print("Keeper saved the ball ! NO GOAL")
    else:
        print("Goal, you have to be better !")
        ki_score = ki_score +1 
        
def score():
    print(f" Your score is    : {pl_score} \n Computer score is: {ki_score}")
    

def result():
    print(f''' Here are our result:
                Your score {pl_score}
                Computer score {ki_score}''')
    if pl_score > ki_score:
        print("Great game, you won!")
    elif pl_score == ki_score:
        print("Remis!")
    else:
        print("You lost the game, try again!")



while n_penalties <=8:
    penalty_ki()
    score()
    penalty_pl()
    score()
result()