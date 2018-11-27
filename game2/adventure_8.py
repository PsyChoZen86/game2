import random

debug = 0

#########################################

def debug_1():
    if (debug == 1):
        print("###")
        print("list_r: ", list_r)
        print("princess: ", princess)
        print("pos: ", pos)
        print("room: ", room)
        print("heading: ", heading)
        print("###")
        
def debug_attack():
    if (debug == 2):
        print("###")
        print("monster_pos=",monster_pos)
        print("Player : hp:" + str(player_hp) + " arm:" + str(player_armor) + " st:" + str(player_status) + " lst: " + str(player_last_status))
        print("Monster: hp:" + str(monster_hp) + " arm:" + str(monster_armor) + " st:" + str(monster_status) + " lst: " + str(monster_last_status))
        print("monster_list" + str(monster_list))
        print("###")
        
def debug_attack_internal():
    if debug == 3:
        print("###")        
        print("Input:")
        print("status=",status)
        print("last_status=",last_status)
        print("power=",power)
        print("other_armor=",other_armor)
        print("other_health=",others_health)
        print("###")

########################################

config_file = "adventure_6.txt"

with open(config_file, "r") as config_obj:
    for line in config_obj:
        list_1 = config_obj.read().splitlines()             # split at linebreak > write to list
        list_2 = []
        for i in list_1:                                    # for element in list: split > write to sublist
            list_2.append(i.split())
            list_r = []
        x = 0
        while x < len(list_2):                              # for every index in list_2
            dict_1 = {}
            for block in list_2[x]:
                block = block.strip(",")  # remove ,
                wort = block.split(":")  # split at :
                dict_1[wort[0]] = int(wort[1])  # make dict from direction : roomnumber
            list_r.append(dict_1)  # append to final list_r
            x = x + 1

###################################################################################

princess = random.randint(1, len(list_r)) 

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

#########################################

def anzahl_zeichen_2(t1, t2):
    if len(t1) >= len(t2):
        l = len(t1) + 60
        return l
    else:
        l = len(t2) + 60
        return l


def textfeld_1(z, t, n):
    return z * anzahl_zeichen_2(text, name) + "\n" + \
           z + t.center(anzahl_zeichen_2(text, name) - 2) + z + "\n" + \
           z + n.center(anzahl_zeichen_2(text, name) - 2) + z + "\n" + \
           z * anzahl_zeichen_2(text, name) + "\n"


def text_center(t):
    return t.center(anzahl_zeichen_2(text, name))



def eingabe():
    a, b = input("Where do you want to go to? \n(type:) move east, move west, move north, move south: ").split()      # return: $move $west
    return a, b


def ausgabe_room():
    print("-" * 82 + "\nYou have entered room " + str(pos) + ". No princess found.")


def move_err():
    print("-" * 82 + "\nYou can't move to " + heading)


def ausgabe_found_princess():
    print("-" * 82 + "\nYou are in room " + str(pos) + ". You have found the princess!")  
    

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

###################################################################################

debug_1()

print("-" * 82)
name = input("Please tell me your name: ")
name = name + "!"
text = "Welcome to the dungeon"
zeichen = "+"

print("\n" + textfeld_1(zeichen, text, name))
print("""Find the princess before she get killed by the monsters.
Don't waste your time.""")

print(text_center("Move!"))

######################################

while (pos != princess):

    debug_1()

    #if (room status: visited - later)
    ausgabe_room()
    
    if pos in monster_list:
        
        monster_pos = pos           #monster refresh here >
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
                    #monster_hp = 50                   #set new
                    #monster_armor = 10
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
                    monster_hp = 50                   #if monster is set to 50 here loop is starting again, breaks at remove
                    monster_armor = 10
                    print("-" * 82)
                    print("You have killed the monster.")
                        
                debug_attack()

            elif command == "run":
                player_status = "run"
                monster_status = monster_status_list[random.randint(0, 1)]
                monster_armor, monster_hp = attack(player_power, player_skill, player_status, player_last_status, monster_status, monster_armor, monster_hp)
                player_armor, player_hp = attack(monster_power, monster_skill, monster_status, monster_last_status, player_status, player_armor, player_hp)
                player_last_status = "attack"
                monster_last_status = monster_status
                # if player_hp >= 0:
                #     heading = subject
                #     if heading in room:
                #         pos = room[heading]
                #         room = list_r[pos - 1]
                #         # room last visited??
                #     else:
                #         move_err()
                

    command, subject = eingabe()

    if (command == "move"):  # add more in-room positions (for rooms with 2 doors at 1 side)
        heading = subject
        if (heading in room):
            pos = room[heading]
            room = list_r[pos - 1]
        else:
            move_err()
    # elif (command == "look"):  # looking at the walls, coming from mapfile every 2nd line for each room
    #     heading = subject
    #     # funktion look(heading)

ausgabe_found_princess()