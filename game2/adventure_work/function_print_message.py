#function to print a text message like that:

#   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   +                             your message                                       +
#   +                                 name                                           +
#   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# your text message:    t     str
# your name:            n     str
# symbol:               s     str
# padding               p     int    + padding text padding +


def print_textfield(t, n, s, p):
        
    text = t
    name = n
    star = s
    padding = p
    
    def count_char(text, name):              # calculating length
        if len(text) >= len(name):
            l = len(text) + padding  # 60
            return l
        else:
            l = len(name) + padding  # 60
            return l


    def textfield(z, t, n):
        return z * count_char(t, n) + "\n" + \
               z + t.center(count_char(t, n) - 2) + z + "\n" + \
               z + n.center(count_char(t, n) - 2) + z + "\n" + \
               z * count_char(t, n) + "\n"
    
    print = textfield(star, text, name)
    
    return print



