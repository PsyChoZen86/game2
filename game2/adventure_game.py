# a simple textadventure
#
# maps are stored in a configfile > adventure_config.txt
# view at the walls are stored in > look_config.txt           <todo: can be merged into one file!
#
# movement:   move direction
# look:       look direction
#
# battlesystem from: import battle_system

import random
import battle_system
import function_read_config
import function_print_message

#########################################
#debug

debug = 0

def debug_1():
    if (debug == 1):
        print("###")
        print("list_r: ", list_r)
        print("princess: ", princess)
        print("pos: ", pos)
        print("room: ", room)
        print("heading: ", heading)
        print("room_l=", str(room_l))
        print("###")
        

########################################
# read config files

list_r = function_read_config.read_config("map_config.txt")
list_l = function_read_config.read_config("look_config.txt")

########################################
# variables

princess = random.randint(1, len(list_r)) 

pos = 1                                    
while pos == princess:
    pos = random.randint(1, len(list_r))       #if pos = pos_princess

room = list_r[pos - 1]
room_l = list_l[pos - 1]

heading = ""
player_hp = 100
monster_list = [2,3,8]

playername = "testplayer"                      #remove!
                      
#########################################
# defs

def input_command():
    a, b = input("Where do you want to do? \n(type:) 'move direction' or 'look direction': ").split()
    return a, b


def print_room():
    print("-" * 82 + "\nYou are in room " + str(pos) + ". No princess found.")


def move_err():
    print("-" * 82 + "\nYou can't move to " + heading)
    
def print_killed_enemy(h):
    print("-" * 82 + "\nYou have killed the enemy! Your health is", h, "HP")


def print_found_princess():
    print("-" * 82 + "\nYou are in room " + str(pos) + ". You have found the princess!")

def print_dead():
    print("-" * 82 + "\nYou are dead!")
    

###################################################################################
# intro

debug_1()

print("-" * 82)
name = playername
name = name + "!"
text = "Welcome to the dungeon"
star = "+"
padding = 60

#print("\n" + textfield_(star, text, name))
print("\n" + function_print_message.print_textfield(text, name, star, padding))
print("""Find the princess before she get killed by the monsters.
Don't waste your time.""")

m = "Move!"
print(m.center(82))

######################################
# mainloop

while pos != princess:
    
    debug_1()

    #if (room status: visited - later)
    print_room()
    
    while pos in monster_list and player_hp >= 0:          
        monster_pos = pos        
        player_hp = battle_system.battle(player_hp, name)
        if player_hp >= 0:
            monster_list.remove(monster_pos)
            print_killed_enemy(player_hp)
        elif player_hp <= 0:
            monster_list.remove(monster_pos)            
            print_dead()
        
    command, subject = input_command()

    if (command == "move"):
        heading = subject
        if (heading in room):
            pos = int(room[heading])
            room = list_r[pos - 1]
        else:
            move_err()
            
    elif (command == "look"):
        heading = subject
        if (heading in room_l):
            view = room_l[heading]
            print("-" * 82)
            print(view)
                    
print_found_princess()


