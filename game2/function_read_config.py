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
        data = config_obj.read()                            # read file to data
        list_1 = data.splitlines()                          # split data to list_1
        list_2 = []
        for i in list_1:                                    # for element in list: split > write to sublist
            list_2.append(i.split("_"))
            list_r = []
        x = 0
        while x < len(list_2):                              # for every index in list_2
            dict_1 = {}
            for block in list_2[x]:
                block = block.strip(",")                    # remove ,
                word = block.split(":")                     # split at :
                dict_1[word[0]] = word[1]                   # make dict from direction : roomnumber as string                      
            list_r.append(dict_1)                           # append to final list_r
            x = x + 1               

    return list_r
