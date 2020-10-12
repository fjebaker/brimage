def remap(x, s1, s2, d1, d2):
    """ helper functio: remaps x in range s1-s2 into d1-d2 """
    return (((x - s1) / (s2 - s1)) * (d2 - d1)) + d1
