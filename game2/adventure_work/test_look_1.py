list_l = [{'north': 'a door', 'east': 'a door'}, {'west': 'a door', 'east': 'a door'}, {'west': 'a door', 'north': 'a door', 'east': 'a door'}]

pos = 1

room = list_l[pos - 1]

heading = "north"

def eingabe():
    a, b = input("Where do you want to go to? \n(type:) move east, move west, move north, move south: ").split()      # return: $move $west
    return a, b

while True:
    
    command, subject = eingabe()
       
    if (command == "look"):
        heading = subject
        if (heading in room):
            view = room[heading]
            print("There is", view)
            
      #  else:
           # move_err()

#view = room[heading]
#print(view)