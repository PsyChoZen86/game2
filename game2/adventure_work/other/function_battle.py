#Variables:
    
pos = 1                                    
while pos == princess:
    pos = random.randint(1, len(list_r))       #if pos = pos_princess

room = list_r[pos - 1]

heading = ""
player_hp = 100
player_power = 30
player_armor = 10
player_skill = 1
player_status = ""
player_last_status = ""

monster_list = [2,3,8]

monster_hp = 50
monster_power = 30                             
monster_armor = 10
monster_skill = 1
monster_status_list = ["attack", "block"]
monster_last_status =""        


###################################################################################

#Function:

def attack(power, skill, status, last_status, other_status, others_armor, others_health):

    if status == "block":
        power = 0
        
    if last_status == "block":
        #power = int(power * 2)
        power = power * 2

    if other_status == "block":
        #others_armor_new = others_armor * 2  
        others_armor_new = others_armor + 20       #if block: armor + 20
    elif other_status == "run":                    # not implemented
        others_armor_new = int(others_armor / 2)  
    else:
        others_armor_new = others_armor

    if skill == 1:
        precision_low = 6
        precision_high = 11
    elif player_skill == 2:
        precision_low = 3
        precision_high = 8
    elif skill == 3:
        precision_low = 0
        precision_high = 5

    precision = random.randint(precision_low, precision_high)

    #power = power - precision                      #switch off to disable precision
              
    if power <= 0:
        power = 0
        
#    print("###")
#    print("Input:")
#    print("pos=",pos)
#    print("monster_pos=",monster_pos)
#    print("status=",status)
#    print("last_status=",last_status)
#    print("power=",power)
#    print("others_armor=",others_armor)
#    print("others_health=",others_health)
#    print(str(monster_list))
#    print("###")
      
    x = others_armor_new - power
    if x <= 0:
        others_health = others_health + x
        others_armor_new = 0
    else:
        others_health = others_health         #remove!
        others_armor_new = others_armor_new   #remove!
        if others_armor_new <= 0:
            others_armor_new = 0
    
    if other_status == "block" and others_armor_new > others_armor:
        others_armor_new = others_armor
    
    if status == "run":
        others_armor_new = others_armor_new + (others_armor / 2)
        if others_armor_new <= 0:
            others_armor_new = 0

    if others_health <= 0:
        others_health = 0
       
    return others_armor_new, others_health

#################################################################

#call function in game:   #monster will be erased from monster_list but: 
                         #monster hp is not refreshed after monster-kill > next monster has hp=0 > fight not starting
    
    if pos in monster_list:
        
        monster_pos = pos           #monster refresh here?
        while monster_hp > 0:
            
            print("There is a monster.")
            print("-" * 82)
            print("Your Health: " + str(player_hp) + ":" + str(player_armor) + " - Monsters health: " + str(monster_hp) + ":" + str(monster_armor))
            command = input("What you're going to do: 'attack', 'block' or 'run'?")

            if command == "attack":
                player_status = "attack"
                monster_status = monster_status_list[random.randint(0, 1)]
                monster_armor, monster_hp = attack(player_power, player_skill, player_status, player_last_status, monster_status, monster_armor, monster_hp)
                player_armor, player_hp = attack(monster_power, monster_skill, monster_status, monster_last_status,player_status, player_armor, player_hp)
                player_last_status = "attack"
                monster_last_status = monster_status
                if monster_hp <= 0:
                    monster_list.remove(monster_pos)
                    print(str(monster_list))
                    #monster_hp = 50                   #if monster is set to 50 here loop is starting again, breaks at remove
                    #monster_armor = 10                #if monster is set to 50 here loop is starting again, breaks at remove
                    print("-" * 82)
                    print("You have killed the monster.")

                debug_attack()

            elif command == "block":
                player_status = "block"
                monster_status = monster_status_list[random.randint(0, 1)]
                monster_armor, monster_hp = attack(player_power, player_skill, player_status, player_last_status, monster_status, monster_armor, monster_hp)
                player_armor, player_hp = attack(monster_power, monster_skill, monster_status, monster_last_status, player_status, player_armor, player_hp)
                player_last_status = "block"
                monster_last_status = monster_status
                if monster_hp <= 0:
                    monster_list.remove(monster_pos)
                    print(str(monster_list))
                    #monster_hp = 50                   #if monster is set to 50 here loop is starting again, breaks at remove
                    #monster_armor = 10                #if monster is set to 50 here loop is starting again, breaks at remove
                    print("-" * 82)
                    print("You have killed the monster.")
    
