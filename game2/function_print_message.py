# function to print a text message like that:

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
            x = len(text) + padding  # 60
            return x
        else:
            x = len(name) + padding  # 60
            return x

    def textfield(z, t, n):
        return z * count_char(t, n) + "\n" + \
               z + t.center(count_char(t, n) - 2) + z + "\n" + \
               z + n.center(count_char(t, n) - 2) + z + "\n" + \
               z * count_char(t, n) + "\n"

    print_text = textfield(star, text, name)

    return print_text
