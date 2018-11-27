import random
import battle_system
import function_read_config

#########################################
#debug

debug = 1

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
#read config files

list_r = function_read_config.read_config("adventure_config.txt")
list_l = function_read_config.read_config("look_config.txt")



########################################
#variables

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
#defs

def count_char_2(t1, t2):
    if len(t1) >= len(t2):
        l = len(t1) + 60
        return l
    else:
        l = len(t2) + 60
        return l


def textfield_1(z, t, n):
    return z * count_char_2(text, name) + "\n" + \
           z + t.center(count_char_2(text, name) - 2) + z + "\n" + \
           z + n.center(count_char_2(text, name) - 2) + z + "\n" + \
           z * count_char_2(text, name) + "\n"


def text_center(t):
    return t.center(count_char_2(text, name))



def eingabe():
    a, b = input("Where do you want to go to? \n(type:) move east, move west, move north, move south: ").split()      # return: $move $west
    return a, b


def ausgabe_room():
    print("-" * 82 + "\nYou have entered room " + str(pos) + ". No princess found.")


def move_err():
    print("-" * 82 + "\nYou can't move to " + heading)


def ausgabe_found_princess():
    print("-" * 82 + "\nYou are in room " + str(pos) + ". You have found the princess!")  
    


###################################################################################
#intro

debug_1()

print("-" * 82)
name = playername
name = name + "!"
text = "Welcome to the dungeon"
star = "+"

print("\n" + textfield_1(star, text, name))
print("""Find the princess before she get killed by the monsters.
Don't waste your time.""")

print(text_center("Move!"))

######################################
#mainloop

while (pos != princess):

    debug_1()

    #if (room status: visited - later)
    ausgabe_room()
    
    if pos in monster_list:
        
        monster_pos = pos        
        battle_system.battle(player_hp, name)

    command, subject = eingabe()

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
            print("There is a", view)

ausgabe_found_princess()
