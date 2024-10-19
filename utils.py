def bin_to_int(x):
    """ Helper function to turn binary number to deciaml """
    my_int = int(x, base=2)
    return my_int


def int_to_bin(x,n):
    """ Helper function to turn decimal to binary number containing n digits """
    bn = bin(x)[2:].zfill(n)
    return bn
        

def int_to_int(x,n):
    """ Add description """
    bn = bin(x)[2:]
    my_int = 0
    for (i,bit) in enumerate(bn[::-1]):
        if bit == "1":
            my_int += 2**(n+i)
    return my_int