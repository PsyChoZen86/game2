import random
import get_playername

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
        

########################################

config_file = "adventure_config.txt"

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

monster_list = [2,3,8]
                      

#########################################

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

debug_1()

print("-" * 82)
name = get_playername.playername()
name = name + "!"
text = "Welcome to the dungeon"
star = "+"

print("\n" + textfield_1(star, text, name))
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

            #if command == "attack":


            #elif command == "block":


            #elif command == "run":

                

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
