def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Values do not match.")
#    elif len(strand_a) < 1 or len(strand_b) < 1:
#        raise ValueError("Not enough values to unpack.")
    
    distance = 0
    for i, j in zip(strand_a, strand_b):
        if i != j:
            distance += 1
    return distance

