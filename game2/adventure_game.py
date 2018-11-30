import random
import battle_system
import function_read_config
import function_print_message

# Blooshed Mansion
# a simple textadventure
#
# maps are stored in a configfile > adventure_config.txt
# view at the walls are stored in > look_config.txt
# todo: look and map can be merged into one file!
# todo: room description + status visited message from configfile
#
# Bug: If the player avoids the fight monster will be removed from
# monster_list. If not, the fight starts again.
#
# movement:   move direction
# look:       look direction
#
# battlesystem from: import battle_system


def game(game2_playername):
    
    #########################################
    # debug

    debug = 0

    def debug_1():
        if debug == 1:
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

    princess = random.randint(6, len(list_r)) 

    pos = 1                                    
    
    room = list_r[pos - 1]                                                      # load initial room from roomlist
    room_l = list_l[pos - 1]                                                    # load initial room from viewlist

    heading = ""
    player_hp = 100
    monster_list = [3, 6, 8, 9, 11, 13, 15, 17, 19]                             # need random function

    name = game2_playername
                          
    #########################################
    # defs

    def input_command():
        a, b = input("Where do you want to do? \n(type:) 'move direction' or 'look direction': ").split()
        return a, b

    def print_room():
        print("-" * 82 + "\nYou are in room " + str(pos) + ". No princess found.")

    def move_err():
        print("-" * 82 + "\nYou can't move to " + heading)

    def input_err():
        m = "Input Error!"
        print("-" * 82 + "\n" + m.center(82))
        print("\nYou have to input two words. 'command' and 'direction'")
        print("(type:) 'move direction' or 'look direction': ")

    def print_intro(n):
        pl_name = n
        pl_name = pl_name + "!"
        text = "Welcome to Bloodshed Mansion"
        star = "+"
        padding = 60
        print("-" * 82)
        print("\n" + function_print_message.print_textfield(text, pl_name, star, padding))
        print("Find the princess before she get killed by the monsters.\nDon't waste your time.")

        m = "Move!"
        print(m.center(82))
        
    def print_enemy_killed(h):
        print("-" * 82 + "\nYou have killed the enemy! Your health is", h, "HP")

    def print_enemy_not_killed(h):
        print("-" * 82 + "\nYou didn't killed the enemy! Your health is", h, "HP")

    def print_found_princess():
        print("-" * 82 + "\nYou are in room " + str(pos) + ". You have found the princess!")

    def print_dead():
        print("-" * 82 + "\nYou are dead!")

    ######################################
    # mainloop

    debug_1()
    print_intro(name)

    while pos != princess:
        
        try:        
            debug_1()
            print_room()                                                        # player position
            
            while pos in monster_list and player_hp >= 0:          
                monster_pos = pos                                               # set monster pos to player pos
                player_hp, monster_alive = battle_system.battle(player_hp, name)   # battle
                if player_hp >= 0:
                    if monster_alive is False:
                        monster_list.remove(monster_pos)                        # delete monster from monster_list
                        print_enemy_killed(player_hp)
                    elif monster_alive is True:
                        monster_list.remove(monster_pos)                    # Bug: if enemy is not removed > next battle
                        print_enemy_not_killed(player_hp)                       # enemy HP will be max on
                elif player_hp <= 0:                                            # next room entry!!
                    monster_list.remove(monster_pos)            
                    print_dead()
                    
            command, subject = input_command()

            if command == "move":
                heading = subject
                if heading in room:
                    pos = int(room[heading])                                    # get next room pos from dict
                    room = list_r[pos - 1]                                      # switch room to pos
                    room_l = list_l[pos - 1]                
                else:
                    move_err()
                    
            elif command == "look":
                heading = subject
                if heading in room_l:
                    view = room_l[heading]                                       # get view text from roomlist
                    print("-" * 82)
                    print(view)
                
        except ValueError:                                                       # catch if only one input
            input_err()
                        
    print_found_princess()
