import random as r                                                                                     
import time
import pygame


def Game(playername):
    
    pygame.mixer.init()
    pygame.mixer.music.load("Scott_Holmes_-_04_-_Teamwork.mp3")
    pygame.mixer.music.play()
    
    
    shoot_direction = ["left", "right", "middle"]                                                          
    ki_score  = 0                                                                                          #computer score
    pl_score  = 0                                                                                          #player score
    n_penalties = 0                                                                                        #total number of penalties
    ppl_penalties = 0 
    print("\n")
    print(f"Welcome {playername}, you'll play as Cristiano Ronaldo")
    print("You are able to shoot and dive in the following directions: left, right or middle ")
    time.sleep(1)
  
    
    #function for the player penalty
    def penalty_pl(ppl_score, ppl_penalties):        
        #ppl_score = 0
        #ppl_penalties = 0
        ppl_penalties =  ppl_penalties + 1                                                                 #update the total number of penalties
        
        valid = False                                                                                      #is input valid?
        while not valid:
            pl_directionshoot = input("Where do you want to shoot?   ").lower()                            #the choice as input, where to shoot
            if pl_directionshoot in shoot_direction:                                                       #validation 
                valid = True                                                                               #validation passed
                
        ki_jumpdirection  = r.choice (shoot_direction)                                                     #computer choice as random, where to jump
        print("\n")
        time.sleep(1)
        print(f"The Goalkeeper is jumping to the {ki_jumpdirection}")                                      #where is the goaly jumping
        
        
        if pl_directionshoot == "left" and ki_jumpdirection =="right":                                     
            print("Keeper saved the ball ! NO GOAL")
        elif pl_directionshoot == "right" and ki_jumpdirection =="left":                                   
            print("Keeper saved the ball ! NO GOAL")
        elif pl_directionshoot == "middle" and ki_jumpdirection =="middle":                                
            print("Keeper saved the ball ! NO GOAL")                                                       
        else:                                                                                                                         
            print("GOOOAAAL, nice shot !")                                                                 
            ppl_score = ppl_score +  1
        return ppl_score, ppl_penalties                 #player score update


            
    #function for the Computer penalty        
    def penalty_ki(pki_score, pki_penalties):                                                                                                                                                                 #load the variable for total number of penalties
        #pki_penalties = 0                           
        #pki_score        = 0                                                                                   #load the variable for the score of the Computer
        pki_penalties  = pki_penalties + 1                                                          #update the total number of penalties
        
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
            pki_score = pki_score    +1                                                                      #Computer score update
        return pki_score , pki_penalties
            
    #function for the actually score        
    def score(sc_kiscore,sc_plscore):                                                                                           
        print(f" Your score is    : {sc_plscore} \n Computer score is: {sc_kiscore}")                          #show the actual score
        

    #function for the result
    def result(res_kiscore, res_plscore):
        pygame.mixer.music.stop()
        print(f''' Here are our result:                                                                                
                    Your score {res_plscore}
                    Computer score {res_kiscore}''')                                                          #showcase for the result
        if res_plscore > res_kiscore:                                                                            #compare the player score and computer score
            print("Great game, you won!")                                                                  
        elif res_plscore == res_kiscore:                                                                         #compare the player score and computer score
            print("Remis!")                                                                                
        else:                                                                                              #every other result
            print("You lost the game, try again!")

    ##########################################################
    #loop for the penalties until 10
    while n_penalties <=8:                                                                                
        ki_score ,  n_penalties = penalty_ki(ki_score, n_penalties)                                                                                       #start function penalty_ki
        score(ki_score , pl_score )                                                                                                  #show the score
        pl_score ,  n_penalties= penalty_pl(pl_score, n_penalties)                                                                                       #start function penalty_pl
        score(ki_score, pl_score)                                                                                                            #show the score
    result(ki_score, pl_score)                                                                                                                #after 10 penalties, show the result



