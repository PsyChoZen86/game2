import random as r                                                                                     
import time                                                                                            
import title_penalty
shoot_direction = ["left", "right", "middle"]                                                          
ki_score  = 0                                                                                          #computer score
pl_score  = 0                                                                                          #player score
n_penalties = 0                                                                                        #total number of penalties

title_penalty.titel()                                                                                  

#function for the player penalty
def penalty_pl():                                                                                      
    global n_penalties                                                                                 
    global pl_score                                                                                    
    n_penalties = n_penalties +1                                                                       #update the total number of penalties
    
    valid = False                                                                                      #is input valid?
    while not valid:
        pl_directionshoot = input("Where do you want to shoot?   ").lower()                            #the choice as input, where to shoot
        if pl_directionshoot in shoot_direction:                                                       #validation 
            valid = True                                                                               #validation passed
            
    ki_jumpdirection  = r.choice (shoot_direction)                                                     #computer choice as random, where to jump
    print("\n")
    print(f"The Goalkeeper is jumping to the {ki_jumpdirection}")                                      #where is the goaly jumping
    
    
    if pl_directionshoot == "left" and ki_jumpdirection =="right":                                     
        print("Keeper saved the ball ! NO GOAL")                                                       
    elif pl_directionshoot == "right" and ki_jumpdirection =="left":                                   
        print("Keeper saved the ball ! NO GOAL")                                                       
    elif pl_directionshoot == "middle" and ki_jumpdirection =="middle":                                
        print("Keeper saved the ball ! NO GOAL")                                                       
    else:                                                                                                                         
        print("GOOOAAAL, nice shot !")                                                                 
        pl_score = pl_score +1                                                                         #player score update


        
#function for the Computer penalty        
def penalty_ki():                                                                                      
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
    time.sleep(1)
    print(f"The shot is going to the {ki_directionshoot}")   
    
    if ki_directionshoot == "left" and pl_jumpdirection =="right":                                    
        print("You saved the ball! Great Keeper skills! NO GOAL")                                     
    elif ki_directionshoot == "right" and pl_jumpdirection =="left":                                   
        print("Wow, what a save! NO GOAL")                                                             
    elif ki_directionshoot == "middle" and pl_jumpdirection =="middle":                              
        print("Keeper saved the ball ! NO GOAL")                                                       
    else:
        print("Goal, you have to be better !")                                                         
        ki_score = ki_score +1                                                                         #Computer score update

        
#function for the actually score        
def score():                                                                                           
    print(f" Your score is    : {pl_score} \n Computer score is: {ki_score}")                          #show the actual score
    

#function for the result
def result():                                                                                        
    print(f''' Here are our result:                                                                                
                Your score {pl_score}
                Computer score {ki_score}''')                                                          #showcase for the result
    if pl_score > ki_score:                                                                            #compare the player score and computer score
        print("Great game, you won!")                                                                  
    elif pl_score == ki_score:                                                                         #compare the player score and computer score
        print("Remis!")                                                                                
    else:                                                                                              #every other result
        print("You lost the game, try again!")                                                         

##########################################################
#loop for the penalties until 10

while n_penalties <=8:                                                                                
    penalty_ki()                                                                                       #start function penalty_ki
    score()                                                                                            #show the score
    penalty_pl()                                                                                       #start function penalty_pl
    score()                                                                                            #show the score
result()                                                                                               #after 10 penalties, show the result
