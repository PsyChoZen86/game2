import random as r                                                                                     #import random
import time                                                                                            #import time
import überschrift
shoot_direction = ["left", "right", "middle"]                                                          #shootdirection
ki_score  = 0                                                                                          #computer score
pl_score  = 0                                                                                          #player score
n_penalties = 0                                                                                        #total number of penalties

title_penalty.titel()                                                                                   #title with stars and name

def penalty_pl():                                                                                      #function for the player penalty
    global n_penalties                                                                                 #load the variable for total number of penalties
    global pl_score                                                                                    #load the variable for the score of the player
    n_penalties = n_penalties +1                                                                       #update the total number of penalties
    
    valid = False                                                                                      #is input valid?
    while not valid:
        pl_directionshoot = input("Where do you want to shoot?   ").lower()                            #the choice as input, where to shoot
        if pl_directionshoot in shoot_direction:                                                       #validation 
            valid = True                                                                               #validation passed
            
    ki_jumpdirection  = r.choice (shoot_direction)                                                     #computer choice as random, where to jump
    print("\n")
    print(f"The Goalkeeper is jumping to the {ki_jumpdirection}")                                      #where is the goaly jumping
    
    
    if pl_directionshoot == "left" and ki_jumpdirection =="right":                                     #compare the shoot- and jump-direction
        print("Keeper saved the ball ! NO GOAL")                                                       #for no goal
    elif pl_directionshoot == "right" and ki_jumpdirection =="left":                                   #compare the shoot- and jump-direction
        print("Keeper saved the ball ! NO GOAL")                                                       #for no goal
    elif pl_directionshoot == "middle" and ki_jumpdirection =="middle":                                #compare the shoot- and jump-direction
        print("Keeper saved the ball ! NO GOAL")                                                       #for no goal
    else:                                                                                                                         
        print("GOOOAAAL, nice shot !")                                                                 #goal
        pl_score = pl_score +1                                                                         #player score update
    
def penalty_ki():                                                                                      #function for the Computer penalty
    global n_penalties                                                                                 #load the variable for total number of penalties
    global ki_score                                                                                    #load the variable for the score of the Computer
    n_penalties = n_penalties +1                                                                       #update the total number of penalties
    
    valid2 = False                                                                                     #is input valid?
    while not valid2:
        pl_jumpdirection = input("Where do you want to dive?   ").lower()                              #the choice as input, where jump
        if pl_jumpdirection in shoot_direction:                                                        #validation 
            valid2 = True                                                                              #validation passed
    ki_directionshoot = r.choice (shoot_direction)                                                     #computer choice as random, where to shoot
    print("\n")
    print(f"The shot is going to the {ki_directionshoot}")                                             #where is the goaly jumping
    if ki_directionshoot == "left" and pl_jumpdirection =="right":                                     #compare the shoot- and jump-direction
        print("You saved the ball! Great Keeper skills! NO GOAL")                                      #for no goal
    elif ki_directionshoot == "right" and pl_jumpdirection =="left":                                   #compare the shoot- and jump-direction
        print("Wow, what a save! NO GOAL")                                                             #for no goal
    elif ki_directionshoot == "middle" and pl_jumpdirection =="middle":                                #compare the shoot- and jump-direction
        print("Keeper saved the ball ! NO GOAL")                                                       #for no goal
    else:
        print("Goal, you have to be better !")                                                         #goal
        ki_score = ki_score +1                                                                         #Computer score update
        
def score():                                                                                           #function for the actually score
    print(f" Your score is    : {pl_score} \n Computer score is: {ki_score}")                          #show the actual score
    

def result():                                                                                          #function for theresult
    print(f''' Here are our result:                                                                                
                Your score {pl_score}
                Computer score {ki_score}''')                                                          #showcase for the result
    if pl_score > ki_score:                                                                            #compare the player score and computer score
        print("Great game, you won!")                                                                  #win
    elif pl_score == ki_score:                                                                         #compare the player score and computer score
        print("Remis!")                                                                                #remis
    else:                                                                                              #every other result
        print("You lost the game, try again!")                                                         #lost



while n_penalties <=10:                                                                                #loop for the penalties until 10
    penalty_ki()                                                                                       #start function penalty_ki
    score()                                                                                            #show the score
    penalty_pl()                                                                                       #start function penalty_pl
    score()                                                                                            #show the score
result()                                                                                               #after 10 penalties, show the result
