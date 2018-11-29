#a simple turn based battle system with randomly generated damage
#and remaining enemy hit points display.
#future versions should include: more battle options


def battle(player_hp, player_name):
    
    #module needed for random damage calculation
    import random

    #for testing
    #player_hp = 100
    #player_name = "Test"

    #variables
    enemy_hp = 50 #indicator for remaining enemy hitpoints
    hp_symbol = "*" #symbol used for visualisation
    battle_active = True #indicator for battle loop (while battle is active)
    player_choice = "o" #placeholder for player choice variable
    attack_power = 0 #stores the last attacks value
    minimum = 8 #minimum damage value for player
    maximum = 18 #maximum damage value for player
    buff_duration = 99 #placeholder for buff counter
    enemy_alive = True #indicator to know if enemy died or player fled

    #returns number of remaining HP as symbols to visualize it
    def hp_graphic(hp, sym):
        return hp * sym
    #returns a string to print out the possible choices
    def choose():
        return ("""
        (a)ttack
        (b)attlestance
        (r)un

    Choose your destiny: """)


    ########## main code ##########

    print ("\n!!!! Enemy appeared. !!!!")
    input("(hit enter to proceed)")

    while battle_active == True and enemy_hp > 0:
        
        #display remaining enemy hp
        print ("\nTroll HP:", enemy_hp) 
        print (hp_graphic(enemy_hp, hp_symbol))
        print ("\n\n" + player_name + " HP:", player_hp)
        print (hp_graphic(player_hp, hp_symbol))
        
        #ask for player choice
        player_choice = input (choose())
        
        #attack -> calculate and print damage
        if player_choice == "a": 
            if buff_duration < 3:
                attack_power = random.randint(minimum + 2, maximum + 2)
                print ("\nYou did", attack_power, "damage.")
                enemy_hp = enemy_hp - attack_power
                buff_duration = buff_duration + 1
            else:
                attack_power = random.randint(minimum, maximum)
                print ("\nYou did", attack_power, "damage.")
                enemy_hp = enemy_hp - attack_power
            
            attack_power = random.randint(1, 10)
                
            if attack_power > 3:
                player_hp = player_hp - attack_power
                print ("\nThe Troll did", attack_power, "damage.")
            else:
                print ("\nYou dodged the attack.")
                
        #battlestance -> 3 rounds
        elif player_choice =="b":
            buff_duration = 0
            print("\nYour minimum and maximum damage raises by 2 for 3 rounds!")
            
                
        #run -> success -> print escape message & leave loop
        elif player_choice == "r":
            if random.randint(1,10) > 4:
                print ("You ran away...")
                battle_active = False
            else:
                attack_power = random.randint(1,10)
                player_hp = player_hp - attack_power
                print ("\nThe Troll did", attack_power, "damage.")
                buff_duration = buff_duration + 1
                
            
        #other command -> print error message
        else:
            print ("\nPlease try again!\n")
        
    print ("The battle is over!\n")
    
    #check if enemy is still alive based on hp remaining
    if enemy_hp <= 0:
        enemy_alive = False

    return player_hp, enemy_alive

#battle(100, "Test")