# read from configfile
#
# Configfile:
#
# north:7 east:2
# west:1 east:3
# west:2 north:8 east:4
# west:3 north:12 east:9
#
# one line for one room
# direction:room behind door
#
# list_r = [{'north': '7', 'east': '2'}, {'west': '1', 'east': '3'}, {'west': '2', 'north': '8', 'east': '4'} .....]
#
#


def read_config(f):

    config_file = f

    with open(config_file, "r") as config_obj:
        for line in config_obj:                                 # line is not used!!
            list_1 = config_obj.read().splitlines()             # split at linebreak > write to list
            list_2 = []
            for i in list_1:                                    # for element in list: split > write to sublist
                list_2.append(i.split("_"))
                list_r = []
            x = 0
            while x < len(list_2):                              # for every index in list_2
                dict_1 = {}
                for block in list_2[x]:
                    block = block.strip(",")                    # remove ,
                    wort = block.split(":")                     # split at :
                    dict_1[wort[0]] = wort[1]                   # make dict from direction : roomnumber as string                      
                list_r.append(dict_1)                           # append to final list_r
                x = x + 1                

    return list_r
