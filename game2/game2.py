#import both games (Penalty Shoot-out and Adventure)
import adventure_game
#import penalty_mit_fehler
#import function_print_message for starting border around the name (Credits Roman)
import function_print_message
#main function menu
def mainmenu():
    #safing input as playername
    playername = input("Welcome to game2. Please state your name in the following line.\n")
    #giving variable allocation
    name = playername
    name = name + "!"
    text = "Main Menu"
    star = "+"
    padding = 60
    #gave variable allocation
    #print function_print_message
    print("\n" + function_print_message.print_textfield(text, name, star, padding))
    #menu text
    print("    Welcome",playername, """to game2. For this menu and the following games,
    you will use the console to play and control your units.""")
    game_choice = input("""    We have a collection of 2 text adventures right now.
    You can choose between a Penalty shoot-out or an Adventure Game.
    Type "shoot-out" for playing the Penalty shoot-out or type
    "adventure" for the adventure game!\n""")
    #execute adventure or shootout
    if game_choice == "adventure":
        adventure_game_6.game(playername)
    elif game_choice == "shoot-out":
        Penalty_Final.game(playername)    
    else:
        print("Wrong input. Menu is restarting!\n")
        mainmenu()
mainmenu()