#import both games (Penalty Shoot-out and Adventure)
#import adventure_8
#import penalty_mit_fehler

def mainmenu():
    star = "*" 
    playername = input("Welcome to game2. Please state your name in the following line.\n")
    length = len(playername)+2
    #input safed as playername
    #stars surrounding the Name
    print(star * length + (2 * star))
    print(star+ " "+ playername + " " + star)
    print(star * length + (2 * star))
    #menu text
    print("    Welcome",playername, """to game2. For this menu and the following games,/
    you will use the console to play and control your units.""")
    input("""    We have a collection of 2 text adventures right now.
    You can choose between a Penalty shoot-out or an Adventure Game.
    Type "shoot-out" for playing the Penalty shoot-out or type
    "adventure" for the adventure game!\n""")
    #execute adventure or shootout
    if input == "adventure":
        print("asdfafg")
    #adventure_8.funktionsname
    elif input == "shoot-out":
        print("adsfasdf")
    #penalty_mit_fehler.funktionsname    
    else:
        print("Wrong input. Menu is restarting!\n")
        mainmenu()
mainmenu()